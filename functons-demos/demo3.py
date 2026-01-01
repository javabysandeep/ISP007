def is_perfect(number):
    factors_sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            factors_sum += i

    return factors_sum == number


print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(496))
