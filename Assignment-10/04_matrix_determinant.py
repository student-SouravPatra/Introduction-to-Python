import numpy as np

A = np.array([
    [1, 3],
    [2, 4]
])

determinant = np.linalg.det(A)

print("Matrix:")
print(A)

print("Determinant:", determinant)
