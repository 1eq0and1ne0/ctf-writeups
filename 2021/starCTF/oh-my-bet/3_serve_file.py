import os
from binascii import unhexlify


sniffed_hex_stream = 'HEX_STREAM_FROM_PREVIOUS_STEP'
filename = 'payload'
port = 1234

with open(filename, 'wb') as f:
	f.write(unhexlify(sniffed_hex_stream))

os.system(f'nc -lvp {port} < {filename}')
