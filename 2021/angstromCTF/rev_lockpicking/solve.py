from pwn import *
from binascii import hexlify
import sys, os

LOCAL = True
HOST, PORT = 'shell.actf.co', 21702
FILE = '/home/ubuntu/anstrongCTF/lockpicking'

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

if LOCAL:
	r = process(FILE, aslr=False)
else:
	r = remote(HOST, PORT)

if LOCAL and 'gdb' in sys.argv:
	gdb.attach(r, 'break *0x555555554000+0x15A0\ndisable 1\nadd-symbol-file lock_struct.o 0')
	# gcc -g -c lock_struct.c
	# add-symbol-file lock_struct.o 0
	# p (struct lock_struct)*$rdi

# 4 -> 2 -> 1 -> 2(-) -> 3 -> 2 -> 0
# enable ctrl4 (22 11 7)
r.sendline('I'*6) # 'i' * 22
r.sendline('m'*11)
r.sendline('o'*7)

# enable ctrl2 (6 37 13)
r.sendline('i'*12)
r.sendline('M'*18) # 'm'*26
r.sendline('o'*6)
r.sendline('!')

# enable ctrl1 (9 8 7)
r.sendline('i'*3)
r.sendline('m'*15)
r.sendline('O'*6) # 'o'*50
r.sendline('!')

# disable ctrl2
r.sendline('!')

# enable ctrl3
# -

# enable ctrl2 (6 37 13)
r.sendline('I'*3) # 'i'*25
r.sendline('M'*15) # 'm'*29
r.sendline('o'*6)
r.sendline('!')

# enable ctl0 (0 0 0)
r.sendline('I' * 6) #'i'*22
r.sendline('m'*7)
r.sendline('O' * 13) # 'o'*43
r.interactive()

# max 164
