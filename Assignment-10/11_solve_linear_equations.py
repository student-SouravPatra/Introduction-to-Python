import numpy as np

A = np.array([
    [3, -5],
    [4, -2]
])

B = np.array([10, 7])

solution = np.linalg.solve(A, B)

print("Value of x:", solution[0])
print("Value of y:", solution[1])
