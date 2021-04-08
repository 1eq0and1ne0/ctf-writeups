from pwn import *

LOCAL = True
HOST, PORT = 'crypto.2021.chall.actf.co', 21600

if LOCAL:
	r = process(['python3', '/home/ubuntu/anstrongCTF/chall.py'])
else:
	r = remote(HOST, PORT)

class Generator():
	DIGITS = 8
	def __init__(self, seed):
		self.seed = seed
		assert(len(str(self.seed)) == self.DIGITS)

	def getNum(self):
		self.seed = int(str(self.seed**2).rjust(self.DIGITS*2, "0")[self.DIGITS//2:self.DIGITS + self.DIGITS//2])
		return self.seed

def get_next_nums(x, y):
	r1 = Generator(x)
	r2 = Generator(y)
	return [r1.getNum() * r2.getNum() for i in range(4)]


r.sendlineafter('random number [g]? ', 'r')
n1 = int(r.recvline()[:-1].decode())
r.sendlineafter('random number [g]? ', 'r')
n2 = int(r.recvline()[:-1].decode())
r.sendlineafter('random number [g]? ', 'r')
n3 = int(r.recvline()[:-1].decode())

x = int(n1 ** 0.5)
print('searching')
while x > 1:
	if n1 % x == 0:
		a, b, c, d = get_next_nums(x, n1 // x)
		if a == n2 and b == n3:
			print('Found')
			print(a, b, c)
			r.sendlineafter('random number [g]? ', 'g')
			r.sendlineafter('generated? ', str(c))
			r.sendlineafter('generated? ', str(d))
			print(r.recvall().decode())
			break
	x -= 1
