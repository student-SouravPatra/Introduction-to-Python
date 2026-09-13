import numpy as np

marks = np.array([
    [50, 85, 80],
    [60, 95, 35],
    [70, 65, 68],
    [85, 55, 65],
    [45, 95, 35]
])

minimum = np.min(marks[1])

print("Minimum marks of Student 2:", minimum)
