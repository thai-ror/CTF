argv= [ 0xBF, 0x86, 0xE2, 0x90,
	0x47, 0x42, 0xC3, 0xE7,
	0x95, 0xA0, 0x91, 0x41,
	0x05, 0x80, 0xE4, 0xA0,
        
	0xA2, 0xD3, 0x47, 0x45,
	0x84, 0xBF, 0xB1, 0xFD,
	0xCD, 0x07, 0x18, 0xC6,
	0x67, 0x33, 0x00, 0x00
]

lst=[]

c0=c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=c13=c14=c15=c16=c17=c18=c19=cc20=c21=c22=c23=c24=c25=c26=c27=0
def r1():
    for i in range(32,128):
        if i^0xF2==argv[1]:
            print "c0",hex(i),chr(i)
            lst.append(i)
            break
    for i in range(32,128):
        if i^0xD7==argv[0]:
            print "c1",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0xF2==argv[6]:
            print "c2",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0x91==argv[2]:
            print "c3",hex(i),chr(i)
            lst.append(i)
            break


def r2():
    for i in range(32,128):
        if i^0xA1==argv[3]:
            print "c4",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0x34==argv[4]:
            print "c5",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0x76==argv[5]:
            print "c6",hex(i),chr(i)
            lst.append(i)
            break

    for i in range(32,128):
        if i^0xF2==argv[8]:
            print "c7",hex(i),chr(i)
            lst.append(i)
            break

def r3():
    for i in range(32,128):
        if i^0xD7==argv[7]:
            print "c8",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0xF2==argv[13]:
            print "c9",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0x91==argv[9]:
            print "c10",hex(i),chr(i)
            lst.append(i)
            break
    for i in range(32,128):
        if i^0xA1==argv[10]:
            print "c11",hex(i),chr(i)
            lst.append(i)
            break
        
def r4():
    for i in range(32,128):
        if i^0x34==argv[11]:
            print "c12",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0x76==argv[12]:
            print "c13",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0xF2==argv[15]:
            print "c14",hex(i),chr(i)
            lst.append(i)
            break
    for i in range(32,128):
        if i^0xD7==argv[14]:
            print "c15",hex(i),chr(i)
            lst.append(i)
            break

def r5():
    for i in range(32,128):
        if i^0xF2==argv[20]:
            print "c16",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0x91==argv[16]:
            print "c17",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0xA1==argv[17]:
            print "c18",hex(i),chr(i)
            lst.append(i)
            break
    for i in range(32,128):
        if i^0x34==argv[18]:
            print "c19",hex(i),chr(i)
            lst.append(i)
            break

def r6():
    for i in range(32,128):
        if i^0x76==argv[19]:
            print "c20",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0xF2==argv[22]:
            print "c21",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0xD7==argv[21]:
            print "c22",hex(i),chr(i)
            lst.append(i)
            break
    for i in range(32,128):
        if i^0xF2==argv[27]:
            print "c23",hex(i),chr(i)
            lst.append(i)
            break
def r7():
    for i in range(32,128):
        if i^0x91==argv[23]:
            print "c24",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0xA1==argv[24]:
            print "c25",hex(i),chr(i)
            lst.append(i)
            break
        
    for i in range(32,128):
        if i^0x34==argv[25]:
            print "c26",hex(i),chr(i)
            lst.append(i)
            break
    for i in range(32,128):
        if i^0x76==argv[26]:
            print "c27",hex(i),chr(i)
            lst.append(i)
            break

        
r1()
r2()
r3()
r4()
r5()
r6()
r7()
fl=''
#
print lst
for i in lst:
    fl+=str(chr(i))
fl+='g3'
print "Flag",fl+"_"*(30-len(fl))
#print " ".join(c1,c2,c3)
