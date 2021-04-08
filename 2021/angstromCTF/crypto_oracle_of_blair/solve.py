from pwn import *
from binascii import hexlify, unhexlify
from Crypto.Util.Padding import unpad

LOCAL = True
TEST = False
HOST, PORT = 'crypto.2021.chall.actf.co', 21112
FILE = ['python3', '/home/ubuntu/anstrongCTF/server.py']

if LOCAL:
	r = process(FILE)
else:
	r = remote(HOST, PORT)


def decrypt(data):
	r.sendlineafter('give input: ', data)
	return r.recvline()[:-1].decode()

def xor_blocks(b1, b2, block_size=16):
	b1 = unhexlify(b1.rjust(block_size * 2, '0'))
	b2 = unhexlify(b2.rjust(block_size * 2, '0'))
	return hexlify(bytes([b1[i] ^ b2[i] for i in range(block_size)])).decode()
	

split_blocks = lambda m: [m[i:i+32] for i in range(0, len(m), 32)]

if TEST:
	secret = 'aa' * 16 + 'bb' * 16
else:
	# on server
	# 7b7d 				 	- 2 blocks (32 bytes)
	# 7b7dAAAAAAAAAAAAAA 	- 2 blocks (32 bytes) 
	# 7b7dAAAAAAAAAAAAAAAA	- 3 blocks (48 bytes)
	# flag size = 32-7 = 25
	secret = '7b7dAAAAAAAAAAAAAA'

m1 = decrypt('00' * 16 + '00' * 32 + '00' * 16)
m2 = decrypt('00' * 16 + secret + '00' * 16)
b1 = split_blocks(m1)
b2 = split_blocks(m2)
print(b1)
print(b2)

pt2 = xor_blocks(b1[-1], b2[-1])
print(pt2)

m1 = decrypt('00' * 16 + '00' * 16 + pt2)
m2 = decrypt('00' * 16 + secret)
b1 = split_blocks(m1)
b2 = split_blocks(m2)
print(b1)
print(b2)

pt1 = xor_blocks(b1[-1], b2[-1])
print(pt1)

print(unhexlify(pt1+pt2))
