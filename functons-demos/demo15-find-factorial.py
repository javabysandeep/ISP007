#5 ! = 1 * 2 * 3* 4 * 5
def find_factorial(number):
    result = 1
    for i in range(1,number+1):
        result *= i
    return result

print(find_factorial(1))
print(find_factorial(2))
print(find_factorial(3))
print(find_factorial(4))
print(find_factorial(5))
print(find_factorial(6))


