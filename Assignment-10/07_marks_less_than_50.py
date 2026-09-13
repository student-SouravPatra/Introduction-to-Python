import numpy as np

marks = np.array([
    [50, 85, 80],
    [60, 95, 35],
    [70, 65, 68],
    [85, 55, 65],
    [45, 95, 35]
])

result = marks[marks[:, 0] < 50, 0]

print("Marks less than 50 in Subject 1:")
print(result)
