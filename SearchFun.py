#Search Fun

import re

str1="Hello , welcome in the world of python"
pattern1="python"
if(re.search(pattern1,str1)):
    print("Found")
else:
    print("Not Found")
