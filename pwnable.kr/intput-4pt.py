#ssh input2@pwnable.kr -p2222
from pwn import *
context(arch = 'amd64', os = 'linux')

sh = ssh(host='pwnable.kr', user='input2', password='guest', port=2222)
proc=sh.interactive()
