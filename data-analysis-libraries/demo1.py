import numpy as np

numbers = [56, 54, 50, 75, 70, 75, 59]
print(type(numbers)) #<class 'list'>
print(numbers)

array1 = np.array(numbers)
print(type(array1)) #<class 'numpy.ndarray'>
print(array1)
print('min = ',array1.min())
print('max = ',array1.max())
print('mean = ',array1.mean())
#array2 = array1 #reference copy
array2 = array1.copy() #new array
print(array2)
print('id= ',id(array1))
print('id= ',id(array2))

