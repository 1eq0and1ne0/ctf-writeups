from pwn import *
from binascii import hexlify
import sys, os

LOCAL = True
HOST, PORT = 'shell.actf.co', 21701
FILE = '/home/ubuntu/anstrongCTF/jailbreak'

if LOCAL:
	r = process(FILE)
else:
	r = remote(HOST, PORT)

r.sendlineafter('What would you like to do?\n', 'look around')
r.sendlineafter('What would you like to do?\n', 'pick the snake up')
r.sendlineafter('What would you like to do?\n', 'throw the snake at kmh')
r.sendlineafter('What would you like to do?\n', 'pry the bars open')
r.sendlineafter('What would you like to do?\n', 'look around')

x = 1337
actions = []
while (x != 1):
	print(x)
	if x % 2 == 0:
		actions.append('press the red button')
	else:
		actions.append('press the green button')
		x -= 1
	x /= 2

actions = actions[::-1]

for action in actions:
	r.sendlineafter('What would you like to do?\n', action)

r.sendlineafter('What would you like to do?\n', 'bananarama')

r.interactive()

