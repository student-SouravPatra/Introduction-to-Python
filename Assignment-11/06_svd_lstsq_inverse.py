Q6 — 8×8 matrix: inv(), svd(), lstsq()
import numpy as np
from scipy import linalg

A = np.array([
    [2, 1, 0, 0, 0, 0, 0, 0],
    [1, 3, 1, 0, 0, 0, 0, 0],
    [0, 1, 4, 1, 0, 0, 0, 0],
    [0, 0, 1, 5, 1, 0, 0, 0],
    [0, 0, 0, 1, 6, 1, 0, 0],
    [0, 0, 0, 0, 1, 7, 1, 0],
    [0, 0, 0, 0, 0, 1, 8, 1],
    [0, 0, 0, 0, 0, 0, 1, 9]
], dtype=float)

# 1. Inverse
inverse = linalg.inv(A)

print("Inverse of A:")
print(inverse)

# 2. SVD
U, S, Vh = linalg.svd(A)

print("\nU:")
print(U)

print("\nSingular Values:")
print(S)

print("\nVh:")
print(Vh)

# 3. Least Squares
b = np.arange(1, 9, dtype=float)

x, residuals, rank, singular_values = linalg.lstsq(A, b)

print("\nLeast Squares Solution:")
print(x)

print("\nResiduals:")
print(residuals)

print("\nRank:")
print(rank)

print("\nSingular Values:")
print(singular_values)
