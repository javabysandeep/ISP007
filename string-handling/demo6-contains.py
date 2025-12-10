string = 'good morning'
# check if d is present in string or not
isPresent = False
for i in string:
    if i == 'd':
        isPresent = True
        break

if isPresent:
    print('yes')
else:
    print('no')

print('using in operator')
print('d' in string)#True
print('x' in string)#False