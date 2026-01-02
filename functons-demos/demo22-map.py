numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for number in numbers:
    result.append(number * number)

print(numbers)
print(result)
print("using map function")


def square_function1(number):
    return number * number


square_function2 = lambda number: number * number

print(list(map(square_function1, numbers)))
print(list(map(square_function2, numbers)))
print(list(map(lambda number: number * number, numbers)))
