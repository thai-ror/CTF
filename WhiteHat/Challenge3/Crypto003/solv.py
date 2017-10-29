letter = "abcdefghijklmnopqrstuvwxyz"
faces = ["=]]",":')",":0","_._!", ":'(",";]","=))","=)",":~)","(-_-)","-_-",":))","~_~","<3",":/","^_^",";))","*_*",":)","-.-","^^",":()",";)","@@",":>",":v"]
def x():
           with open("faces.txt", "r") as file:
                      data = file.read()

           for i in range(len(faces)):
               print letter[i], faces[i]
               data = data.replace(faces[i], letter[i])
           print len(letter), len(faces)
           print data

x()
#f l 4 g _ c t f _ i s _ n i g h t m a r e

