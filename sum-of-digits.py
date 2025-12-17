number = int(input("enter the number"))
originalNumber=number
sumOfDigits = 0
while number > 0:
    digit = number % 10
    sumOfDigits += digit
    number //= 10

print('sum of digits is = ', sumOfDigits)
print('sum of digits of ', originalNumber, 'is ', sumOfDigits)
s='sum of digits of ', originalNumber, 'is ', sumOfDigits
print(type(s))

