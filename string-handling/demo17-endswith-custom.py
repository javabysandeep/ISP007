str = 'good morning'
key = 'g'
keyLength = len(key)
i = 0
j = len(str)-keyLength
flag = True
while i < keyLength:
    if key[i] != str[j]:
        flag = False
        break
    i = i + 1
    j = j + 1

print('present' if flag else 'not present')
