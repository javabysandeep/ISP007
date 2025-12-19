numbers = [10, 20, 30, 40, 25]
print('before reverse')
print(numbers)
print('after reverse')
left = 0
right = len(numbers) - 1
while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp
    left += 1
    right -= 1

print(numbers)
