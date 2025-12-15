str = 'good morning'
key='g'
count=0

for item in str:
    if item == key:
        count+=1

print('g is present = ',count)
print(str.count('g'))
print(str.count('o'))
print(str.count('d'))