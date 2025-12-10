s1 = "good morning"

#left to right
print(s1.index('m'))#5
print(s1.index('o'))#1 -> first occurrence index
#print(s1.index('x'))#ValueError: substring not found

print(s1.find('m'))#5
print(s1.find('o'))#1
print(s1.find('x'))#-1


#right to left
print(s1.rindex('m'))#5
print(s1.rindex('o'))#6
print(s1.rfind('m'))#5
print(s1.rfind('o'))#6