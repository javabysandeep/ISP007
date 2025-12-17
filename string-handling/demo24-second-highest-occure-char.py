str = 'xabcabcccbyy'
# output - second highest = b
charIntMap = {}
for char in str:
    if char in charIntMap.keys():
        charIntMap[char] += 1
    else:
        charIntMap[char] = 1

print(charIntMap)
