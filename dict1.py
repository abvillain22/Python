st=dict()

st["name"]="abhay"
st["age"]=20
st["branch"]="C.S"

print("dict after insert name age branch")
print(st)
print()

st["branch"]="C.S.E"

print("dict after update branch")
print(st)
print()

i="course"
if(i in st):
    pass
else:
    st["course"]="B.Tech"


print("dict after insert course")
print(st)
print()

del st["age"]

print("dict after del age")
print(st)
print()

st.clear()

print("dict after alear all entries")
print(st)

del st
