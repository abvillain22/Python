import re
st=input("enter a string = ")
x=re.findall("^[\w\-]+",st)
print(x)
