numbers = list(range(10))
print("numbers {} are of type {}".format(numbers, type(numbers)))
# numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] are of type <class 'list'>
print(numbers[0:len(numbers) - 1:1])  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

numbers[0]='abc'#list is mutable
print(numbers)
