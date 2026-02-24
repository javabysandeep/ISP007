import numpy as np

array_of_arrays = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
print(array_of_arrays)
print(array_of_arrays[0])  # [1 2 3]
print(array_of_arrays[1])  # [4 5 6]
print(array_of_arrays[2])  # [7 8 9]

print('accessing first array elements',
      array_of_arrays[0][0],
      array_of_arrays[0][1],
      array_of_arrays[0][2])

print('accessing second array elements',
      array_of_arrays[1][0],
      array_of_arrays[1][1],
      array_of_arrays[1][2])

print('accessing third array elements',
      array_of_arrays[2][0],
      array_of_arrays[2][1],
      array_of_arrays[2][2])