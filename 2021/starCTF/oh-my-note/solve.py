import time
import datetime
import random
import string


def get_random_id():
    alphabet = list(string.ascii_lowercase + string.digits)
    return ''.join([random.choice(alphabet) for _ in range(32)])

post_at = '2021-01-15 02:29 UTC'
note_id = 'lj40n2p9qj9xkzy3zfzz7pucm6dmjg1u'

timestamp = datetime.datetime.strptime(post_at, "%Y-%m-%d %H:%M UTC").replace(tzinfo=datetime.timezone.utc).timestamp()
print(timestamp)

current_note_id = ''
while note_id != current_note_id:
	random.seed(timestamp)
	user_id = get_random_id()

	random.seed(user_id + post_at)
	current_note_id = get_random_id()

	timestamp = round(((timestamp * 10000) + 1) / 10000, 4)
	if timestamp % 10 == 0:
		print(timestamp)

print(user_id)
