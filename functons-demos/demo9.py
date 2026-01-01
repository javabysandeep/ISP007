def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


print(add(100, 200))
print(add(100, 200, 300))
print(add(100, 200, 300, 400))
