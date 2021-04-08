from pwn import *
from binascii import hexlify
import sys, os

LOCAL = True
HOST, PORT = 'shell.actf.co', 21700

if LOCAL:
	r = process('/home/ubuntu/anstrongCTF/infinity_gauntlet')
else:
	r = remote(HOST, PORT)

k = 1

flag = ['X'] * 50

while True:
	r.recvuntil('===\n')
	eq = r.recvline()[:-1].decode()
	log.info(eq)

	f, res = eq.split(' = ')
	f_name, args = f.split('(')
	args = args[:-1].split(', ')

	
	if f_name == 'foo':
		if res == '?':
			x = int(args[0]) ^ (int(args[1]) + 1) ^ 0x539
		elif args[0] == '?':
			x = int(res) ^ (int(args[1]) + 1) ^ 0x539
		else:
			x = (int(args[0]) ^ int(res) ^ 0x539) - 1
	else:
		if res == '?':
			x = (int(args[2]) + 1) * int(args[1]) + int(args[0])
		elif args[0] == '?':
			x = int(res) - int(args[1]) * (int(args[2]) + 1)
		elif args[1] == '?':
			x = (int(res) - int(args[0]))//(int(args[2])+1)
		else:
			x = ((int(res) - int(args[0]))//((int(args[1]))%1337))-1
	
	if (k > 49):
		pos = ((x >> 8) - (k % 255))
		print(f'k={k} pos={pos} x={hex(x)}')
		flag[pos] = chr(((x & 0xff) ^ (17 * pos))&0xff)
		print(''.join(flag))
	r.sendline(str(x))
	k += 1	
