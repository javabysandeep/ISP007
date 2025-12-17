str = 'ab12abc12xyz566'
# output = ababcxyz1212566
alphaList = []
digitList = []
for i in str:
    if i.isalpha():
        alphaList.append(i)
    if i.isdigit():
        digitList.append(i)

print(alphaList,digitList)