import numpy as np

marks = np.array([
    [50, 85, 80],
    [60, 95, 35],
    [70, 65, 68],
    [85, 55, 65],
    [45, 95, 35]
])

count = np.sum(marks[:, 1] > 80)

print("Number of students scoring more than 80 in Subject 2:", count)
