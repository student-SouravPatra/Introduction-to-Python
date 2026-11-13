# Question 1: NumPy Marks Analysis

import numpy as np

# Create a NumPy array containing marks of 5 students
# Each row represents a student
# Each column represents a subject

marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [76, 80, 85],
    [89, 75, 90],
    [95, 92, 88]
])

# Display the marks array
print("Marks of Students:")
print(marks)

# Display shape and size of the array
print("\nShape of Array:", marks.shape)
print("Size of Array:", marks.size)

# Find minimum marks in Subject 1
min_subject1 = np.min(marks[:, 0])

print("\nMinimum Marks in Subject 1:")
print(min_subject1)

# Calculate subject-wise minimum marks
subject_min = np.min(marks, axis=0)

print("\nSubject-wise Minimum Marks:")
print(subject_min)

# Calculate subject-wise maximum marks
subject_max = np.max(marks, axis=0)

print("\nSubject-wise Maximum Marks:")
print(subject_max)

# Calculate total marks obtained by each student
total_marks = np.sum(marks, axis=1)

print("\nTotal Marks of Each Student:")
print(total_marks)

# Calculate student ranks based on total marks
rank = np.argsort(np.argsort(-total_marks)) + 1

print("\nStudent Rankings:")

for i in range(len(total_marks)):
    print("Student", i + 1,
          "- Total Marks:", total_marks[i],
          "- Rank:", rank[i])


#Output
Marks of Students:
[[85 90 78]
 [92 88 95]
 [76 80 85]
 [89 75 90]
 [95 92 88]]

Shape of Array: (5, 3)
Size of Array: 15

Minimum Marks in Subject 1:
76

Subject-wise Minimum Marks:
[76 75 78]

Subject-wise Maximum Marks:
[95 92 95]

Total Marks of Each Student:
[253 275 241 254 275]

Student Rankings:
Student 1 - Total Marks: 253 - Rank: 4
Student 2 - Total Marks: 275 - Rank: 1
Student 3 - Total Marks: 241 - Rank: 5
Student 4 - Total Marks: 254 - Rank: 3
Student 5 - Total Marks: 275 - Rank: 2
