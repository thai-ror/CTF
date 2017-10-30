from pwn import *
context(os='linux', arch='i386')
r=process('./bai_3_150')
gdb.attach(r, '''
break *0x08048ca8 
''')
r.interactive()
r.close()

