Q4 — 4×4 matrix: transpose and rank using SciPy
import numpy as np
from scipy import linalg

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [2, 4, 6, 8],
    [1, 3, 5, 7]
], dtype=float)

# Transpose
transpose = A.T

# Rank
rank = np.linalg.matrix_rank(A)

print("Matrix A:")
print(A)

print("\nTranspose of A:")
print(transpose)

print("\nRank of A:")
print(rank)
