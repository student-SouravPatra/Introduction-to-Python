# Question 2: Perform operations using Python dictionaries

# Dictionary containing student names and their subject-wise marks
students = {
    "Alice": {
        "Python": 85,
        "Network": 72,
        "DBMS": 90
    },
    "Bob": {
        "Python": 92,
        "Network": 80,
        "DBMS": 88
    },
    "Charlie": {
        "Python": 78,
        "Network": 65,
        "DBMS": 82
    },
    "David": {
        "Python": 95,
        "Network": 70,
        "DBMS": 89
    },
    "Emma": {
        "Python": 88,
        "Network": 85,
        "DBMS": 91
    }
}

# Display student records
print("Student Records:")
for name, marks in students.items():
    print(name, ":", marks)

# Find the student who scored maximum marks in Python
highest_python = max(
    students,
    key=lambda name: students[name]["Python"]
)

print("\nStudent with Maximum Marks in Python:")
print(highest_python)
print("Marks:", students[highest_python]["Python"])

# Find students who scored less than 75 in Network
print("\nStudents scoring less than 75 in Network:")

for name, marks in students.items():
    if marks["Network"] < 75:
        print(name, ":", marks["Network"])


#Output
Student Records:
Alice : {'Python': 85, 'Network': 72, 'DBMS': 90}
Bob : {'Python': 92, 'Network': 80, 'DBMS': 88}
Charlie : {'Python': 78, 'Network': 65, 'DBMS': 82}
David : {'Python': 95, 'Network': 70, 'DBMS': 89}
Emma : {'Python': 88, 'Network': 85, 'DBMS': 91}

Student with Maximum Marks in Python:
David
Marks: 95

Students scoring less than 75 in Network:
Alice : 72
Charlie : 65
David : 70
