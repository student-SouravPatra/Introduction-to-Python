import numpy as np

marks = np.array([
    [50, 85, 80],
    [60, 95, 35],
    [70, 65, 68],
    [85, 55, 65],
    [45, 95, 35]
])

print("Marks Array:")
print(marks)

print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))

student_id = np.argmax(np.max(marks, axis=1))
print("Student ID with maximum marks:", student_id)

print("Maximum marks subject-wise:", np.max(marks, axis=0))
print("Average marks subject-wise:", np.mean(marks, axis=0))
