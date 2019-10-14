import random
l=["dog","cat","lion","tiger"]
len1=len(l)
a=random.randint(0,len1)
l2=l[a]
len2=len(l2)
i=0
while(i<len2):
    b=input("enter a char = ")
    if(l2[i]==b):
        print("you are right")
        i+=1
    else:
        print("you are wrong")
