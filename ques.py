st=input("Enter string:")
import re
word=re.split("\s",st)
d={}

for x in word:
    if(x[0] not in d.keys()):
        d[x[0]]=[]
    if(x not in d[x[0]]):
        d[x[0]].append(x)
for y,z in d.items():
    print(y," = ",z)
