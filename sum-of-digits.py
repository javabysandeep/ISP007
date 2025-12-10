number=int(input("enter the number"))
sumOfDigits=0
while number > 0:
    digit = number % 10
    sumOfDigits +=digit
    number //=10

print('sum of digits is = ',sumOfDigits)
