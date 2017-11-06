import base64
s='49714ODgAgQF/7vAzBXD180Q17/MA8ID1xDR08HCzf+919IDzwXGw7k='
fl_decode=base64.b64decode(s)
fl_list=[]
for i in fl_decode:
    fl_list.append(ord(i)^0xFE)


for i  in range(256):
    flag=''  
    for c in fl_list:
        if c+i>=32 and c+i<=128:
            flag+=chr(c+i)
    print i,flag
