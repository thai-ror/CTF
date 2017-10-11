#flag='ffc309e61f2ac3df48d3b9b64fd1720bfb95b460a1235f5d91c4f92ce90dfa516e1b8c49225b808560a9d853980662dc26984e'
flag=['ff', 'c3', '09', 'e6', '1f', '2a', 'c3', 'df', '48', 'd3', 'b9', 'b6', '4f', 'd1', '72', '0b', 'fb', '95', 'b4', '60', 'a1', '23', '5f', '5d', '91', 'c4', 'f9', '2c', 'e9', '0d', 'fa', '51', '6e', '1b', '8c', '49', '22', '5b', '80', '85', '60', 'a9', 'd8', '53', '98', '06', '62', 'dc', '26', '98', '4e']



def rol(x,i,l):
     x=bin(x).replace('0b','')
     #print x,'-->',
     x='0'*(l-len(x))+x
     x=x[i:]+x[0:i]
     #print x
     x=eval('0b'+x)
     return x

#rotate right
def ror(x,i):
     x=bin(x).replace('0b','')
     l=len(x)
     #print x,'-->',
     xx=x[l-(i):l]
     xx=xx[::-1]
     x=xx+x[0:l-i]
     #print x
     x=eval('0b'+x)
     return x


#shift left
def shl(x,i):
     s=2
     for i in range(i-1):
          s=s*2
     return x*s


def shr(x,i):
     s=2
     for i in range(i-1):
          s=s*2
     return x/s


def sar(x,i):
     s=2
     for i in range(i-1):
          s=s*2
     x=bin(x).replace('0b','')
     if x[0]=='1':
          x=eval('0b'+x)
          x=-x          
     return x/s

#flag='ffc309e61f2ac3df48d3b9b64fd1720bfb95b460a1235f5d91c4f92ce90dfa516e1b8c49225b808560a9d853980662dc26984e'
#str_input=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','-','*','/','~','!','@','#','$','%','^','&','*','(',')','_','=','?','.',',','<','>','`',';',':','[',']','{','}']
str_input='a'
len_str=len(str_input)
v4=0x0FFFFFFFF
#ff43a64cc254
#ff43a64cc254
#ff8b2c290b70
s=[]

for i in range(len_str):
     v2 = hex((v4/16) ^ ord(str_input[i])).replace('L','')
     #v4 = v4 & (-shl(ord(str_input[i]),7)) ^ eval(v2);
     #print hex(v4)
     v4 = v4 &(-(shr(ord(str_input[i]),7))|0xFFFFFF00)^eval(v2);
     print hex(v4), v4


