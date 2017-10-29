from pwn import *
import struct
context(os='linux', arch='i386')

def getConn():
    return process('../bin/./heap1') if local else remote('localhost', 1337)
local = True
r = getConn()
gdb.attach(r, '''

break *0x8048538
break *0x08048555
c
''')

r.interactive()
