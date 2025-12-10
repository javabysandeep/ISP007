number = int(input('Enter a number'))
evenCount = 0
oddCount = 0
while number > 0:
    digit = number % 10
    if digit%2==0:
        evenCount += 1
    else:
        oddCount += 1
    number = number // 10

print('number of even digits in a given number', evenCount)
print('number of odd digits in a given number', oddCount)
