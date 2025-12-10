string='   good    morning    '
list=[]
for c in string:
    if c != ' ':
        list.append(c)

print(list)
print("using prebuilt methods")
print(string.rstrip())
print(string.lstrip())
print(string.strip())

