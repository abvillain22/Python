l=["abhay","sharma","suru","saini"]
for i in range(0,len(l)):
    for j in range(len(l)):
        if(len(l[i])<len(l[j])):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
        
