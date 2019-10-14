def eve(x):
    if(x%2==0):
        return 1;

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even=list(filter(eve,l))
print(even)
