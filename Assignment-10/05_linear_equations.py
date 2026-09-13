import numpy as np

A = np.array([
    [2, -1],
    [3, -1]
])

B = np.array([-5, -8])

solution = np.linalg.solve(A, B)

print("Value of x:", solution[0])
print("Value of y:", solution[1])
