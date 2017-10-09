# crypto1.py
from base64 import b64encode, b64decode
import string
from secret import key, flag

L2I = dict(zip(string.uppercase+string.lowercase+string.digits,range(64)))
I2L = dict(zip(range(64),string.uppercase+string.lowercase+string.digits))

flag = b64encode(flag)

ciphertext = ''.join(I2L[(L2I[c] + key) % 64] for c in flag)
print ciphertext

