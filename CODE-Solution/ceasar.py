import string

text="HJXAJY GPHTPR HPL P CPBDG APGTCTV SCP CPXRXIXADE DWL LTGWIGTKD TWI CPBDG RXAQJETG SCP STWHXAQPIHT TWI TAJG UD TWI HGDGTEBT. GPHTPR STHJ TWI HBTAQDGE SCP HEXWHSGPW UD TWI SDXGTE DI TIPTGR HXW CLD TBTGEJH APRXIXADE SCP NGPIXAXB GTLDE. VPAU HX TWI GPTN IPWI GPHPTR HPL CGDQ. CPBDG GDGTEBT HJXAJY GPHTPR HX STSGPVTG HP TCD UD TWI IHDB AJUGTLDE SCP AJUHHTRRJH HGTSPTA CX TWI NGDIHXW UD TWI SAGDL. HXW TUXA SCP HXW ICTADXK WIPTS TKPW CTTQ NATSXL STIPGQTATR CX TGJIPGTIXA SCP BAXU."
alphabet_upper=string.ascii_uppercase
alphabet_lower=string.ascii_lowercase

num='0123456789'
string=""

l_text=len(text)
l_alphabet=len(alphabet_upper)
l_num=len(num)

s=[]

print "MESSAGE:",text,"\n"

for key in range(1,l_alphabet):
     string=""
     for i in text:
          # Upper Case
          if i in alphabet_upper:
               pos=int(alphabet_upper.index(i))-key
               p=alphabet_upper[pos%l_alphabet]
               string =string+p
          # Lower Case
          elif i in alphabet_lower:
               pos=int(alphabet_lower.index(i))-key
               p=alphabet_lower[pos%l_alphabet]
               string =string+p
          else:
               string+=i
     s.append(string)
     
for i in range(len(s)):
     print i+1,s[i]
print s[14][::-1]
