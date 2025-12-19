numbers = [10, 20, 1, 1, 2, 1]
print(numbers)
numbers.append(99)
print(numbers)
print("insert method")
numbers.insert(1, 98)
print(numbers)

print("extend method")
numbers1 = [10, 20, 1, 1, 2, 1]
numbers2 = [11, 13, 13, 14, 15]
numbers2.extend(numbers1)
print(numbers2)

print("remove method")
numbers = [10, 20, 1, 1, 2, 1]
numbers.remove(1)
print(numbers)#[10, 20, 1, 2, 1]
numbers.remove(11)#ValueError: list.remove(x): x not in list

numbers = [10]
numbers.pop()
numbers.pop()#IndexError: pop from empty list
print(numbers) # [10,20,1,1]