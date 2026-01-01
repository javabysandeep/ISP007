numbers = [10,11,23,24,65]

def is_even1(number):
    return number % 2 == 0

is_even2 = lambda number: number % 2 == 0

print(list(filter(is_even1, numbers)))
print(list(filter(is_even2, numbers)))

print('odd numbers',list(filter(lambda number: number % 2 == 1, numbers)))
