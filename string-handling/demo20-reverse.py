str1 = 'good morning'

# syntax start:end:step
print(str1[0:12:1])  # good morning
print(str1[12:0:-1])  # gninrom doo
print(str1[::-1])  # gninrom doog

print("way 02 : using reversed method")
print(''.join(reversed(str1)))
print(type(reversed(str1)))

print("way 03 : using loop")
i = len(str1) - 1
result = ''
while i >= 0:
    result = result + str1[i]
    i = i - 1
print(result)

print("way 04 : using list")
list=[]
i = len(str1) - 1
while i >= 0:
    list.append(str1[i])
    i = i - 1
print(''.join(list))