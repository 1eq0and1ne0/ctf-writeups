from pwn import *

LOCAL = True
HOST, PORT = 'crypto.2021.chall.actf.co', 21602

if LOCAL:
	r = process(['python3', '/home/ubuntu/anstrongCTF/chall_home_crypto.py'])
else:
	r = remote(HOST, PORT)

to_bit_list = lambda x, l: [x >> i & 1 for i in range(l * 8 - 1,-1,-1)]

l = {}
r.sendlineafter('? ', '1')
r.sendlineafter(': ', '00'*16)
l[0] = to_bit_list(int(r.recvline()[:-1].decode(), 16), 16)

r.sendlineafter('? ', '1')
r.sendlineafter(': ', 'FF'*16)
l[1] = to_bit_list(int(r.recvline()[:-1].decode(), 16), 16)

r.sendlineafter('? ', '2')
for i in range(10):
	r.recvuntil('Encrypt this: ')
	n = int(r.recvline()[:-1].decode(),16)

	res = ''.join([str(l[x][i % 128]) for i, x in enumerate(to_bit_list(n, 32))])
	res = int(res,2)
	print('{0:064x}'.format(res))
	r.sendline('{0:064x}'.format(res))

r.interactive()
