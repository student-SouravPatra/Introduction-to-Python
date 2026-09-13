# Assignment 3 - Program 1
# Student Marks using List

# List of student marks
marks = [
    85, 72, 91, 68, 76, 88, 65,
    80, 92, 74, 69, 83, 95, 78,
    87, 71, 90, 66, 84, 79, 73,
    89, 81, 77, 93, 70, 86, 75
]

# 1. Find the average marks
average = sum(marks) / len(marks)

print("Student Marks:", marks)
print("Average Marks:", average)

# 2. Find the number of students scoring more than average
count = 0

for mark in marks:
    if mark > average:
        count += 1

print("Number of students scoring more than average:", count)

# 3. Find the maximum marks
maximum_marks = max(marks)

print("Maximum Marks:", maximum_marks)
