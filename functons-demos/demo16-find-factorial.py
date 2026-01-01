# 4 ! = 1 * 2 * 3* 4
def find_factorial(number):
    if number == 0:
        result = 1
    else:
        result = number * find_factorial(number - 1)
    return result


print(find_factorial(4))
