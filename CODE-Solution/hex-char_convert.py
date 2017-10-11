#hex to char convert
list=[]
s='47414C463930342D32753934386A326F69666A736C6B6C6B34'
[list.append(ord(c)) for c in s.decode('hex')]
char_convert=s.decode('hex')
print 'INT',list
print 'char',char



#str(x) : convert dec,hex,oct,bin to 'dec'
x:dec,hex,oct,bin
        
str(65) ='65'
str(0x41) ='255'
str(0o0101) ='65'
str(0b1000001) ='65'


#chr(x) : convert dec,hex,oct,bin to 'char'
x:dec,hex,oct,bin

decimal: chr(65)='A'
Hexal: chr(0x41)='A'
Octal: chr(0o0101)
Binary : chr(0b1000001)='A'

#ord(x)convert 'char' to int
x:'char'

ord('A'): 65
ord('\x41')=65
ord(u'\u0041')=65

#hex(x):
hex(255)='0xff'
hex(0b1011)='0xb'
hex(1L)='0x1L'





