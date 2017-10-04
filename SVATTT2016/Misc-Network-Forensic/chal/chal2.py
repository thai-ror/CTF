def convert2Int(x):
	return int(x,16)

file=open('chal','rb')
cursor=0
size=0
data=''
d1=""
f= file.read()

while 1:
	if cursor>=len(f): break
	try:
		size=convert2Int(f[cursor]) # size of data
	except:
		break
	cursor =cursor+3
	data=f[cursor:cursor+size]  # data
	print "cursor:",cursor,"size:",size,"data:",data.encode('hex')
	cursor =cursor+size+2  # len of data
	d1+=data

d="504b030414000900080067007c490d0a0d0a4a0000004005000008000000666c61672e747874744c0d6e781ea885789a7f2bcf90d053af8ca8ce2a5a02adef9c980dae7e1e2511a7412e572f55db5a18c900d564b05d16ef326bbf2e9d2e1bbcbcfe641056c8d148bcd5fcfcf57c2cb4504b0708d16f80864a00000040050000504b01021f0014000900080067007c490d0a0d0a4a00000040050000080024000000000000002000000000000000666c61672e7478740a00200000000000010018003c6015c3c748d201c0eba358c748d201c0eba358c748d201504b050600000000010001005a000000800000000000"
print d
print d1.encode('hex')

f=open('result.zip','wb')
f.write(d1)
f.close()

