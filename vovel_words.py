a="Abhay sharma jecrc Student Is not a topper"
import re
#first word of string
x=re.findall(r"^\w+",a)
print(x)

#last word of string
x=re.findall(r"\w+$",a)
print(x)

#start from vowel
x=re.findall(r"\b[aeiouAEIOU]\w+",a)
print(x)

#not start from vovel
x=re.findall(r"\b[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z]\w+",a)
print(x)
