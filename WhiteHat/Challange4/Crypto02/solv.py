# string Input : aaaa
# encode : nuMpXWS80nOsMaT3wxYgn0Bvh/lXkVwNFCOCOLGNrm4=
#
#
#


import sys
from Crypto.Hash import SHA256
from Crypto.Cipher.AES import AESCipher
#from flag import flag as create

def create(s):
           return str(s)

def encrypt(m):
        flag = create()
        key = SHA256.new(flag).digest()
        print "key",key
        
        s = 'something!' + m.decode('base64') + flag

        p = 16 - (len(s) % 16)
        s = s + (chr(p) * p)

        print AESCipher(key).encrypt(s)
        print AESCipher(key).encrypt(s).encode("base64")

m='aaaa'
encrypt(m)



