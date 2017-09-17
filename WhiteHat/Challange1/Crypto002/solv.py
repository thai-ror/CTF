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


#flag: Too_easy_right?
f = open("out.png",'rb')
f1 = open("images.png",'wb')
buf = f.read(8)
key = "W3lld0n3"
while(buf != ""):
    plan = ""
    for each in buf:
        a = bin(ord(each))[2:]
        while(len(a) < 8):
            a = ''.join(['0',a])
        plan = ''.join([plan,a])
    cip = XOR(plan,TextToBin(key))
    i = 0
    while(i < len(buf)*8):
        s = chr(int(str(cip[i:i+8]),2))
        f1.write(s)
        i = i+8
    buf = f.read(8)
f.close()
f1.close()


