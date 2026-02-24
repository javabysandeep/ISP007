import numpy as np

numbers = [56, 54, 50, 75, 70, 75, 59]
# numbers = numbers * 5 # list elements are repeating 5 times.
# print(numbers)

array = np.array(numbers)
print(array)
array = array * 5 # [280 270 250 375 350 375 295]
print(array) #[280 270 250 375 350 375 295]
