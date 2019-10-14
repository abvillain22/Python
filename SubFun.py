import re

str1="hello, welcome in the world of python"
pattern1="hi"
pattern2="hello"
print((re.sub(pattern2,pattern1,str1)))

#the sub fun in the re module can be used to search a pattern in the string and replace it with another string
