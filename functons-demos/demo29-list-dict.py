# convert list of numbers into a dictionary[number, square]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(dict(map(lambda x:(x,x*x),numbers)))


table={}
for num in numbers:
    sq=num**2
    table[num]=sq

print(table)
