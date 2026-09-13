# Assignment 2: Student Names and Marks

# List of 10 student names
students = [
    "Rahul",
    "Amit",
    "Priya",
    "Sneha",
    "Rohan",
    "Ankit",
    "Neha",
    "Suman",
    "Riya",
    "Arjun"
]

# Marks of the 10 students
marks = [85, 72, 91, 68, 91, 76, 88, 65, 80, 72]

# Find maximum and minimum marks
maximum_marks = max(marks)
minimum_marks = min(marks)

print("Student Names:", students)
print("Marks:", marks)

print("\nMaximum Marks:", maximum_marks)
print("Students scoring maximum marks:")

for i in range(len(students)):
    if marks[i] == maximum_marks:
        print(students[i])

print("\nMinimum Marks:", minimum_marks)
print("Students scoring minimum marks:")

for i in range(len(students)):
    if marks[i] == minimum_marks:
        print(students[i])

# Sort the marks
sorted_marks = sorted(marks)

print("\nSorted Marks:", sorted_marks)

# Find duplicate values
duplicates = []

for mark in marks:
    if marks.count(mark) > 1 and mark not in duplicates:
        duplicates.append(mark)

print("Duplicate Marks:", duplicates)
