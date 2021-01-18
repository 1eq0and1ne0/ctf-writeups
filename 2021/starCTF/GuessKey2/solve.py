from pwn import *

r = remote('52.163.228.53', 8082)
mask = 0xffffffffffffffff
i = 0
ans = ''
while ans != b'Nice.':
	i += 1
	r.sendlineafter('mask:', str(mask))
	r.sendlineafter('guess:', str(mask))
	ans = r.recvline()[:-1]
	log.info(str(i))


for i in range(2):
	r.sendlineafter('mask:', '0')
	r.sendlineafter('guess:', str(mask))
	r.recvline()

log.info(r.recvline())
