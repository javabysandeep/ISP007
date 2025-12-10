s1='abc'
s2='abc'
s3='Abc'
print(s1 is s2) # checks the address of ref --> True
print(s1 is s3) # checks the address of ref --> False
print(s1==s2) # content check
x1='A'
x2='B'
print(x1 > x2) #False
print(x1 < x2) #True
print(x1 >=x2) #False
print(x1 <=x2) #True
print(x1 ==x2) #False
print(x1 !=x2) #True