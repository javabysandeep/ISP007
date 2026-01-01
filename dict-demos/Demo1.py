d1 = {}
d2 = {1: 'a', 2: 'b', 3: 'c'}
d3 = d2.copy()
print(d1)
print(d2)
print(d3)
print("accessing the values")
# print(d1['a'])#KeyError: 'a'
if 2 in d2:
    print(d2[2])

# if d2.has_key(2):
#     print(d2[2])