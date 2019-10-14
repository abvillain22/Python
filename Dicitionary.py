#dicitionary is data structure in which we store values as a pair of key and value
#dicitionar is
#in dicitionary the keys must be unique and immutable datatype

d1={"name":"abhay","age":20,"branch":"cs"}
print("name = ",d1["name"])
d1["branch"]="C.S.E"
print("branch = ",d1["branch"])
d1["course"]="B.Tech"
print("course = ",d1["course"])
print(d1)
d1.update({"course":"B.Tech","age":"25"})
l=[[1,2],[1,6]]
d2=dict(l)
print(d2)
del d1["branch"] #d1.popP("branch")
key=d1.keys()
print(key)
value=d1.values()
print(value)
item=d1.items()
print(item)

for key in d1.keys():
    print(key)

for value in d1.values():
    print(value)

for item in d1.items():
    print(item)

for key,value in d1.items():
    print(key,value)

print(sorted(d1.keys()))
print(sorted(d1.values()))
print(sorted(d1.items()))
d1.clear()
del d1

