string='good morning'
#output :  gninrom doog

print('ascending order')
for i in range(0,len(string)):
    print(string[i],end='')

print('\n reverse order')
print(string[::-1]) #gninrom doog

print("using while loop")
i=len(string)-1
while i>=0:
    print(string[i],end='')
    i-=1

print('\n reverse order using for loop')
for i in string[::-1]:
    print(i,end='')