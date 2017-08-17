import subprocess
key ="ffc309e61f2ac3df48d3b9b64fd1720bfb95b460a1235f5d91c4f92ce90dfa516e1b8c49225b808560a9d853980662dc26984e"

x="_"*47
flag=""

for i in range(1,47):
	for c in range(32,128):
		f=open("flag.txt",'w')
		brute_flag=flag+chr(c)+x
		f.write(brute_flag)
		f.close()
		p = subprocess.Popen("./mrc-150 flag.txt", stdout=subprocess.PIPE, shell=True)
		result=p.communicate()[0].strip()
		r=result[2:(i*2)+2]
		o=key[2:(i*2)+2]
		#print r,o
		if r==o:
			flag+=chr(c)
			x="_"*(47-len(flag))
			break
	i+=1
	print flag







