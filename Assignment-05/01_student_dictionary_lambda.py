# Assignment 5 - Student Dictionary
# Using Nested Dictionary and Lambda Function

students = {
    1: {
        "name": "Rahul",
        "department": "CSE",
        "marks": 85
    },
    2: {
        "name": "Amit",
        "department": "CSE",
        "marks": 72
    },
    3: {
        "name": "Priya",
        "department": "IT",
        "marks": 91
    },
    4: {
        "name": "Sneha",
        "department": "ECE",
        "marks": 68
    },
    5: {
        "name": "Rohan",
        "department": "CSE",
        "marks": 88
    }
}

# 1. Sort students according to marks (highest to lowest)
sorted_students = sorted(
    students.items(),
    key=lambda item: item[1]["marks"],
    reverse=True
)

print("Students sorted according to marks:")
for roll_no, details in sorted_students:
    print(
        roll_no,
        details["name"],
        details["department"],
        details["marks"]
    )

# 2. Print the record of the student with the highest marks
highest_student = max(
    students.items(),
    key=lambda item: item[1]["marks"]
)

print("\nStudent with highest marks:")
print("Roll No:", highest_student[0])
print("Name:", highest_student[1]["name"])
print("Department:", highest_student[1]["department"])
print("Marks:", highest_student[1]["marks"])

# 3. Find the average marks
total_marks = sum(
    details["marks"] for details in students.values()
)

average_marks = total_marks / len(students)

print("\nAverage Marks:", average_marks)

# 4. Print students who scored more than the average
print("\nStudents scoring more than average:")

for roll_no, details in students.items():
    if details["marks"] > average_marks:
        print(
            "Roll No:", roll_no,
            "| Name:", details["name"],
            "| Department:", details["department"],
            "| Marks:", details["marks"]
        )
