import requests
import string
import random
from base64 import b64decode, b64encode
from binascii import hexlify
from multiprocessing import Pool

PROXIES = {
	'http': 'http://127.0.0.1:8080',
	'https': 'http://127.0.0.1:8080'
}

HOST, PORT = '52.149.144.45', 8080
LOTTERY_PRICE = 100

def register(username, password):
	print('register')
	r = requests.post(f'http://{HOST}:{PORT}/user/register',
		data={'username': username, 'password': password},
		proxies=PROXIES,
		verify=False
	)
	print(r.json())

def login(username, password):
	print('login')
	r = requests.post(f'http://{HOST}:{PORT}/user/login',
		data={'username': username, 'password': password},
		proxies=PROXIES,
		verify=False
	)
	j = r.json()
	print(j)
	return j['user']['api_token'], j['user']['uuid']

def info(api_token):
	print('info')
	r = requests.get(f'http://{HOST}:{PORT}/user/info',
		params={'api_token': api_token},
		proxies=PROXIES,
		verify=False
	)
	j = r.json()
	print(j)
	return j['user']['coin']

def buy(api_token):
	print('buy')
	r = requests.post(f'http://{HOST}:{PORT}/lottery/buy',
		data={'api_token': api_token},
		proxies=PROXIES,
		verify=False
	)
	j = r.json()
	print(j)
	return b64decode(j['enc'])

def charge(user, enc):
	print('charge')
	r = requests.post(f'http://{HOST}:{PORT}/lottery/charge',
		data={'user': user, 'enc': enc},
		proxies=PROXIES,
		verify=False
	)
	print(r.json())

def lottery_info(enc):
	print('lottery info')
	r = requests.post(f'http://{HOST}:{PORT}/lottery/info',
		data={'enc': enc},
		proxies=PROXIES,
		verify=False
	)
	print(r.json())

def flag(api_token):
	print('flag')
	r = requests.post(f'http://{HOST}:{PORT}/flag',
		data={'api_token': api_token},
		proxies=PROXIES,
		verify=False
	)
	print(r.json())

def get_random_string(n):
	return ''.join(random.choice(string.ascii_lowercase) for i in range(n))

username = get_random_string(16)
password = get_random_string(20)
register(username, password)
token, user = login(username, password)

coins = info(token)
enc = buy(token)
print(f'LOOKING FOR {b64encode(enc)}')
print(coins)
while coins < 10000:
	tmp_username = get_random_string(16)
	tmp_password = get_random_string(20)
	register(tmp_username, tmp_password)
	tmp_token, _ = login(tmp_username, tmp_password)
	tmp_coins = info(tmp_token)
	while tmp_coins >= LOTTERY_PRICE:
		tmp_enc = buy(tmp_token)
		print(b64encode(tmp_enc))
		# lottery_info(b64encode(tmp_enc))
		# lottery_info(b64encode(tmp_enc[:64]+enc[32:-32]+tmp_enc[-32:]))
		# {"lottery":"808fda26-6aa0-43f8-8|ac3-694f573948b3","user":"be7f81|xxx-xxxxxxxxxxxx","user":"yyyyyy|yy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",|"coin":37}
		charge(user, b64encode(tmp_enc[:64]+enc[32:-32]+tmp_enc[-32:]))
		tmp_coins = info(tmp_token)
	coins = info(token)
flag(token)
