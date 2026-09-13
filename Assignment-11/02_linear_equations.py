Q2 — Solve the linear equations using SciPy
import numpy as np
from scipy import linalg

A = np.array([
    [2, 3],
    [4, 2]
], dtype=float)

B = np.array([8, 14], dtype=float)

result = linalg.solve(A, B)

print("Value of x =", result[0])
print("Value of y =", result[1])

