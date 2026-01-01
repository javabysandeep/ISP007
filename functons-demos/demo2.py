# write a function to check if the number is prime or not

def is_prime(number):
    is_prime_flag = True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            is_prime_flag = False
            break
    return is_prime_flag


print(is_prime(10))  # False
print(is_prime(11))  # True
print(is_prime(12))  # False
print(is_prime(13))  # True
