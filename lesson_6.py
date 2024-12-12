Задание 1
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
c3_max = np.max(a[:,2])
r2_max = np.max(a[1,:])
print(c3_max,r2_max)

Задание 2
import numpy as np
a=np.random.randint(-5,6,size=(3,4))
b=np.where(a>0,1,0)
print(a)
print(b)

Задание 3
import numpy as np
def is_magic_square(matrix):
    n = len(matrix)
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    return np.all(row_sums == row_sums[0]) and np.all(col_sums == row_sums[0])
matrix = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
if is_magic_square(matrix):
    print("да она магическая")
else:
    print("Нет не магическая")

Задание 4
import numpy as np
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.transpose())
# Example usage:
matrix = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
if is_symmetric(matrix):
    print("Нет не симетрично")
else:
    print("Да, симетрично")

Задание 5
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
s=np.sum(a,axis=1)
i_max=np.argmax(s)
i_min=np.argmin(s)
print(a[i_max],s[i_max])
print(a[i_min],s[i_min])

задание 6
import numpy as np
def transform_matrix(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        min_index = np.argmin(matrix[i])
        if matrix[i, min_index] % 2 == 0:
            matrix[i, min_index] = 0
        else:
            matrix[i, min_index] = 1
    return matrix

matrix = np.array([[1.5, 2.7, 3.1, 4.2], [5.9, 6.3, 7.1, 8.5], [9.2, 10.8, 11.1, 12.7]])
result = transform_matrix(matrix)
print(result)
