def TextToBin(string):
    res = ""
    for x in string:
        m = format(ord(x),'b')
        while(len(m) < 8):
            m = ''.join(['0',m])
        res = ''.join([res,m])
    return res
def XOR(s1,s2):
    res = ""
    for i in range(0,len(s1),1):
        x = (int(s1[i])) ^ (int(s2[i % len(s2)]))
        res = ''.join([res,str(x)])
    return res

def text2hex(s):
    return hex(ord(s))

#f = open("images.png",'rb')
#f1 = open("out.png",'rb')
#buf = f.read(8)
#encode=f1.read(8)
#for i in encode:
#    print text2hex(i),
    
buf=[0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
encode=[0xde, 0x63, 0x22, 0x2b, 0x69, 0x3a, 0x74, 0x39]

key = ""
flag=""
kk=ord(key[0])
for i in range(len(buf)):
    cip = buf[i]^encode[i]
    flag+=chr(cip)
print flag
#f.close()
#f1.close()


