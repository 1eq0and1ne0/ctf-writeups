from binascii import unhexlify, hexlify
from itertools import cycle

known = b'actf{'
c = 'ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c'
c = unhexlify(c)


for i in range(len(c)-5):
	key = bytes([c[i+k] ^ known[k] for k in range(len(known))])

	print(f'key = {hexlify(key)}, pos = {i}')
	for j in range(len(known)):
		print(''.join([ chr(a ^ b) for (a,b) in zip(c[j:], cycle(key)) ]))


# python3 solve.py | strings | grep actf