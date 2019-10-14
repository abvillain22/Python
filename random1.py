import random
c=1
while(c):
    l=[]
    st="hello"
    st1=st
    st=list(st)
    len1=len(st)
    k=[]
    temp=random.randint(1,len1-2)
    for i in range(0,temp):
        temp1=random.randint(0,len1-2)
        if(temp1 not in k and st[temp1]!=' '):
            st[temp1]='_'
            l.append(temp1)
        k.append(temp1)
    st=''.join(st)
    print(st)
    st=list(st)
    l.sort()
    m=1
    for j in l:
        print("enter char for ",m,"space = ",end="")
        m+=1
        temp2=input()
        st[j]=temp2
    st=''.join(st)
    print("your answer = ",end="")
    print(st)
    print("Right answer = ",end="")
    print(st1)
    if(st==st1):
        print("your answer is right")
    else:
        print("your answer is wrong")
    c=int(input("for again press 1 otherwise 0 = "))
