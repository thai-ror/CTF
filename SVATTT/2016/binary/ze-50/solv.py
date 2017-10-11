def base(x,base):
	x=str(x)
	l=len(x)-1
	s=0
	for i in x:
		if l>=0:
			s+=int(i)*(base**l)
			#print "no.",i,"sum.",s,"exp.",l
			l=l-1
	return s

l=8
for i in range(0,256):
	if base(i,17)==53:
		flag="0"*(l-len(str(i)))+str(i)
		print "SVATTT{%s}" %flag
		break


