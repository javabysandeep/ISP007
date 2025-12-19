# print odd numbers
numbers = [1, 2, 5, 6, 7, 8, 9, 10, 1, 1]
for number in numbers:
    if number % 2 != 0:
        print(number)
print('occurance of 1')
print(numbers.count(1))
