from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x, y: x + y, numbers))

data = ["python", "", "java", "spring", ""]
clean = list(filter(lambda x: len(x) > 0, data))
clean = list(filter(None, data))
print(clean)
