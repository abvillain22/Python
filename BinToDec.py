b=input("enter a binary number = ")
expo=len(b)-1
d=0
for digit in b:
    temp=int(digit)
    d+=temp*(2**expo)
    expo-=1
print("Decimal of ",int(b)," is = ",d)
