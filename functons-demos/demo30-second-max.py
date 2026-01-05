# find the second max number
numbers = [11, 2, 3, 4, 55, 6, 7, 8, 9, 10]

max_num = 0
second_max = 0

for num in numbers:
    if num > max_num:
        second_max = max_num
        max_num = num

    if num > second_max and num < max_num:
        second_max = num


print("max_num:",max_num)
print("second_max:",second_max)
print("using reduce")
