def max_custom(*numbers):
    result = numbers[0]
    for number in numbers:
       if number > result:
           result = number
    return result


print(max_custom(100, 200))
print(max_custom(100, 200, 300))
print(max_custom(100, 200, 300, 400))
