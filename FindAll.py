import re
str1="hello , welcome in the world hello hello hello of python"
pattern="hello"
newstr=re.findall(pattern,str1)
print(newstr)
#the findall fun is used to search a string and return a list of matches of the pattern. If no matches found then it return a empty list

