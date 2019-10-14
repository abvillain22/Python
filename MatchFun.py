#matchFun
import re
str1="Hello, welcome in the world of python"
pattern1=("python")
pattern2=("Hello")
if(re.match(pattern1,str1)):
    print("Found")
else:
    print("Not Found")
    
if(re.match(pattern2,str1)):
    print("Found")
else:
    print("Not Found")

#if the searching pattern is the first word of the str then the match fun works

