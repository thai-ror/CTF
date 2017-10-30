text = open('cipher.txt').readlines()

def xor(str1,str2):
           return "".join(chr(ord(a) ^ ord(b)) for a,b in zip(str1,str2))

o = []
for x in text:
           o += [x.strip().decode('hex')]

passwd = 'I can calculate the motion of heavenly bodies, but not the madness of people.'
o2 = []
for i in xrange(len(o)):
           print i
           o2 += [xor(o[i],o[(i+1)%len(o)])]
           print o2

key=['flag','FLAG','FLag','flag:', 'flag is:', 'Flag is', 'FLAG IS','WhiteHat',"I", "you", "and", "not", " the "]

for c in o2:
           for k in key:
                      print repr(xor(k,c))
