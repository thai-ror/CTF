#thai 1412
#chuoi goc
# so sanh vi tri sai [vt dau den vt tiep theo] --> chr()-->ascii
original="""
Do You Hear The People Song?
[Enjolras:]
Do you fead the people sing?
Singing a song of angry men?
It is the music of a people
Who will not be slaves again!
When the beating of your heart
Echaes the boating of the drums
There is e life abeut to start
When tomorrow comes!

[Combeferre:]
Will you jair in our crusade?
Who will be strong and stand with me?
Beyond the barricade
Is theie a warld you long to see?

[Courfeyrac:]
Then hoin in tre fight
That will give you the right to be free!

[All:]
Do you haar tre people sing?
Singing a song of angry men?
It is the music of a people
Who will not be slaves again!
When the heateng of your heart
Echoes the beating of the drums
There is a life about to start
When tomorrow comes!

[Feuilly:]
Will you give all you can give
So that our banner may advance
Some will fall and some will live
Will you stand up and take your chance?
The cluod of the martyrs
Will water the meadows of France!

[All:]
Do you hear the people sing?
Singing a song of angry men?
It is the music of a people
Who widl not be slaves again!
When the beating of your heart
Echoes the beating of the drums
There is a life about to start
When tomorrow comes
"""

#chuoi seach tren google
real="""
Do You Hear The People Sing?
[Enjolras:]
Do you hear the people sing?
Singing a song of angry men?
It is the music of a people
Who will not be slaves again!
When the beating of your heart
Echoes the beating of the drums
There is a life about to start
When tomorrow comes!

[Combeferre:]
Will you join in our crusade?
Who will be strong and stand with me?
Beyond the barricade
Is there a world you long to see?

[Courfeyrac:]
Then join in the fight
That will give you the right to be free!

[All:]
Do you hear the people sing?
Singing a song of angry men?
It is the music of a people
Who will not be slaves again!
When the beating of your heart
Echoes the beating of the drums
There is a life about to start
When tomorrow comes!

[Feuilly:]
Will you give all you can give
So that our banner may advance
Some will fall and some will live
Will you stand up and take your chance?
The blood of the martyrs
Will water the meadows of France!

[All:]
Do you hear the people sing?
Singing a song of angry men?
It is the music of a people
Who will not be slaves again!
When the beating of your heart
Echoes the beating of the drums
There is a life about to start
When tomorrow comes
"""

original_=original.split('\n')
original_=original_[1:50]
#print original_
real_=real.split('\n')
real_=real_[1:50]
#print real_
l1=len(original_)
l2=len(real_)
i=0
str1=''
str2=''
lst=[]
i=0
t1=[]
t2=[]
flag=''  
while(i<l1):
     print "---------------line",i+1       
     #compare 2 string
     s1=original_[i].strip()
     s2=real_[i].strip()
     #print s1
     #print s2   
     if s1!=' ':
          for z in range(len(s1)):
               #compare 1st position
               if s1[z]!=s2[z]:                 
                    count=0;                 
                    for j in range(z+1,len(s1)):
                         count+=1
                         #compare 2nd position
                         if s1[j]!=s2[j]:
                              
                             print s1[z:j+count-1]
                             print z+1,'-'*count,z+1+count," | ",[z+1,count],"-->",chr(int(str(z+1)+str(count)))
                             flag+=chr(int(str(z+1)+str(count)))
     i+=1
print "flag: ",flag

