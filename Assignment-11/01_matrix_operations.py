#Q1 — Two 3×3 matrices, inverse, determinant, and A A ^ (-1)
import numpy as np
from scipy import linalg


A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
], dtype=float)

B = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 1]
], dtype=float)

# 1. Inverse of matrix A
A_inv = linalg.inv(A)

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nInverse of A:")
print(A_inv)

# 2. Determinant of matrix B
det_B = linalg.det(B)

print("\nDeterminant of B:")
print(det_B)

# 3. A × A^-1
result = A @ A_inv

print("\nA × A^-1:")
print(result)
