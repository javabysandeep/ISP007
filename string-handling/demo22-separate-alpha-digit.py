str = 'ab12abc12xyz566'
# output = ababcxyz1212566
alpha = ''
digit = ''
for i in str:
    if i.isalpha():
        alpha += i
    if i.isdigit():
        digit += i

print(alpha + digit)
