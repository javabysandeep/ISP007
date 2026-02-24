import numpy as np

array_of_arrays = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
for row in array_of_arrays:
    for col in row:
        print(col, " ", end="")
    print()
