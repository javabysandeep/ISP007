# find the second max number
def find_max_second_max(numbers):
    max_num = 0
    second_max = 0

    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num

        if num > second_max and num < max_num:
            second_max = num
    return max_num, second_max

# find the second max number
def f1(numbers):
    max_num = 0
    second_max = 0

    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num

        if num > second_max and num < max_num:
            second_max = num
    return max_num, second_max

# find the second max number
def f2(numbers):
    max_num = 0
    second_max = 0

    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num

        if num > second_max and num < max_num:
            second_max = num
    return max_num, second_max

def f2fjjsajjbvfbvcdbhbhbhadhadvahvdhavdahdv(numbers):
    max_num = 0
    second_max = 0

    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num

        if num > second_max and num < max_num:
            second_max = num
    return max_num, second_max

#print("max_num: and second max ", find_max_second_max([11, 2, 3, 4, 55, 6, 7, 8, 9, 10]))
