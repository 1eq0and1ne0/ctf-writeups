import zlib

def keystream(key):
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]

prefix = 'actf{'
with open('enc', 'rb') as f:
	data = f.read()

# print(data)

for p in range(0x10000):
	key = p.to_bytes(2, 'big')
	k = keystream(key)
	s = ''.join([chr(x ^ next(k)) for x in data])
	if 'actf{' in s:
		print(s)
		break