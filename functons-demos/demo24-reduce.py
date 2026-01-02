numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=0
for number in numbers:
    result +=number
print(result)
print("using function")

def find_sum(numbers):
    result=0
    for number in numbers:
        result += number
    return result
print(find_sum(numbers))


