from gmpy import is_prime
from os import urandom

def bytes_to_num(b):
	return int(b.encode('hex'), 16)

def num_to_bytes(n):
	b = hex(n)[2:-1]
	b = '0' + b if len(b)%2 == 1 else b
	print len(b)%2 == 0
	return b.decode('hex')
	

random_seed = urandom(128)

num = bytes_to_num(random_seed)
print "num",num
# get 2 first prime number from random_seed
p, q = 0,0
while True:
	if is_prime(num):
		p = num
		break
	num+=1

print "p",p

while True:
	if is_prime(num):
		q = num
		break
	num+=1

print "q",q

n = p*q
e = 0x1001

print "n",n

flag = "xxxxxxxxxxxxxxxxxx"

def encrypt(s):
	p = bytes_to_num(s)
	p = pow(p, e, n)
	return num_to_bytes(p)

print "Flag",encrypt(flag).encode('hex')
