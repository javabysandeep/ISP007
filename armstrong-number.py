import math as m
string = input("enter the number")
count = len(string)
number=int(string)
originalNumber = number
sumOfDigits=0
while number > 0:
    digit = number % 10
    sumOfDigits =sumOfDigits + m.pow(digit,count)
    print('loop sum',sumOfDigits)
    number //=10

print('sum of digits is = ',sumOfDigits)

if(originalNumber==sumOfDigits) :
    print('its an armstrong number')
else :
    print('not an armstrong number')
    
    