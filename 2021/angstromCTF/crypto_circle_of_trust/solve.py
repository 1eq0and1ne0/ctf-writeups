import time
from sympy import *
from binascii import unhexlify
from Crypto.Cipher import AES

# Math
# k + r1 = known00
# k + r2 = known01
# k + r3 = known02
# i + sqrt((x ^ 2) - (r1 ^ 2)) = known10
# i + sqrt((x ^ 2) - (r2 ^ 2)) = known11
# i + sqrt((x ^ 2) - (r3 ^ 2)) = known12
#
# r1 = known00 - k
# r2 = known01 - k
# r3 = known02 - k
# i + sqrt((x ^ 2) - (r1 ^ 2)) = known10
# i + sqrt((x ^ 2) - (r2 ^ 2)) = known11
# i + sqrt((x ^ 2) - (r3 ^ 2)) = known12
#
# i + sqrt((x ^ 2) - ((known00 - k) ^ 2)) = known10
# i + sqrt((x ^ 2) - ((known01 - k) ^ 2)) = known11
# i + sqrt((x ^ 2) - ((known02 - k) ^ 2)) = known12
#
# sqrt((x ^ 2) - ((known00 - k) ^ 2)) = known10 - i
# sqrt((x ^ 2) - ((known01 - k) ^ 2)) = known11 - i
# sqrt((x ^ 2) - ((known02 - k) ^ 2)) = known12 - i
#
# (x ^ 2) - ((known00 - k) ^ 2) = (known10 - i) ^ 2
# (x ^ 2) - ((known01 - k) ^ 2) = (known11 - i) ^ 2
# (x ^ 2) - ((known02 - k) ^ 2) = (known12 - i) ^ 2

eqs = []
x, y, z = symbols('x, y, z')
nums = [
	# ('502058966770460576342904432969477477870.9694284169', '397931521047823681786681444905895530031.68007901083'),
	# ('226680564315851381500887149962095517146.7671947536', '557729853971948696530686684926128093170.38807874196'),
	# ('430113374821293184802661616533563795856.7615312825', '487870231335834242530128426766528189123.29663805346')

	('45702021340126875800050711292004769456.2582161398', '310206344424042763368205389299416142157.00357571144'),
	('55221733168602409780894163074078708423.359152279', '347884965613808962474866448418347671739.70270575362'),
	('14782966793385517905459300160069667177.5906950984', '340240003941651543345074540559426291101.69490484699')
]
eqs.append(Eq(pow(x, 2) - pow(Float(nums[0][0], 50)-y, 2), pow(Float(nums[0][1], 50) - z, 2)))
eqs.append(Eq(pow(x, 2) - pow(Float(nums[1][0], 50)-y, 2), pow(Float(nums[1][1], 50) - z, 2)))
eqs.append(Eq(pow(x, 2) - pow(Float(nums[2][0], 50)-y, 2), pow(Float(nums[2][1], 50) - z, 2)))

# x = 297181528875794763822353039056846979930.1701815014
# y = 238418337473105176728553998486723395802
# z = 260780218871543682928099052013041081159

t1=time.time()
# PATCH sympy/core/function.py (n=15 to n=50)
# def nfloat(expr, n=50, exponent=False, dkeys=False):
res = solve(eqs, prec=50)
print(res)
t2=time.time()
print(t2-t1)

for d in res:
	print('x =', round(d[x]))
	print('key (y) =', round(d[y]))
	print('iv (z) =', round(d[z]))

	key = int.to_bytes(int(round(d[y])), 16, 'big')
	iv = int.to_bytes(int(round(d[z])), 16, 'big')

	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	print(cipher.decrypt(unhexlify('838371cd89ad72662eea41f79cb481c9bb5d6fa33a6808ce954441a2990261decadf3c62221d4df514841e18c0b47a76')))
