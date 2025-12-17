numbers = [1, 4, 3, 6, 5]
# output max = 6, smax=5

max = -1
smax = -1

for num in numbers:
    if num > max:
        smax = max
        max = num

    if smax < num < max:
        smax = num

print('max = ', max)
print('smax = ', smax)
