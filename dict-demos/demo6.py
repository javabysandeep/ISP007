d1={}
d1.setdefault("a",1)
d1.setdefault("b",2)
d1.setdefault("c",3)
isKeyPresent = d1.setdefault("c", 30)

print(d1)
print(isKeyPresent)