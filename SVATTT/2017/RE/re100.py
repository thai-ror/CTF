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
def r1():
        i=0xF2^argv[1]
        lst.append(i)
        
        i=0xD7^argv[0]
        lst.append(i)
                
        i=0xF2^argv[6]
        lst.append(i)

        i=0x91^argv[2]
        lst.append(i)
            

def r2():
    
        i=0xA1^argv[3]
        lst.append(i)
    
        i=0x34^argv[4]
        lst.append(i)    
    
        i=0x76^argv[5]
        lst.append(i)
 
        i=0xF2^argv[8]
        lst.append(i)
            

def r3():
    
        i=0xD7^argv[7]
        lst.append(i)

        i=0xF2^argv[13]
        lst.append(i)
            
        i=0x91^argv[9]
        lst.append(i)
            
        i=0xA1^argv[10]
        lst.append(i)
            
        
def r4():
    
        i=0x34^argv[11]
        lst.append(i)
            
          
        i=0x76^argv[12]
        lst.append(i)
            
        i=0xF2^argv[15]
        lst.append(i)
            
   
        i=0xD7^argv[14]
        lst.append(i)
            

def r5():
    
        i=0xF2^argv[20]
        lst.append(i)

        i=0x91^argv[16]
        lst.append(i)

        i=0xA1^argv[17]
        lst.append(i)
            
        i=0x34^argv[18]
        lst.append(i)
            

def r6():
    
        i=0x76^argv[19]
        lst.append(i)

        i=0xF2^argv[22]
        lst.append(i)

    
        i=0xD7^argv[21]
        lst.append(i)
            
        i=0xF2^argv[27]
        lst.append(i)
            
def r7():
    
        i=0x91^argv[23]
        lst.append(i)
 
        i=0xA1^argv[24]
        lst.append(i)

    
        i=0x34^argv[25]
        lst.append(i)
            
    
        i=0x76^argv[26]
        lst.append(i)
            
   
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
