number=int(input("enter the number"))
originalNumber = number
reverse=0
while number>0:
    digit = number % 10
    reverse = reverse *10 + digit
    number //=10

print('reverse number is = ',reverse)

if(originalNumber==reverse) :
    print('its a palindrome number')
else :
    print('not a palindrome number')
    
    