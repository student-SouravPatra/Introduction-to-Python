# Assignment 4 - Program 2
# Employee Dictionary

# Employee dictionary with nested dictionaries
employees = {
    "E1": {
        "name": "Rahul",
        "department": "IT",
        "salary": 50000
    },
    "E2": {
        "name": "Amit",
        "department": "HR",
        "salary": 45000
    },
    "E3": {
        "name": "Priya",
        "department": "Finance",
        "salary": 55000
    },
    "E4": {
        "name": "Sneha",
        "department": "Marketing",
        "salary": 48000
    },
    "E5": {
        "name": "Rohan",
        "department": "IT",
        "salary": 60000
    }
}

# 1. Print the record of employee E1
print("Record of Employee E1:")
print(employees["E1"])

# 2. Print the department of employee E4
print("\nDepartment of Employee E4:")
print(employees["E4"]["department"])

# 3. Find the employee having maximum salary
highest_salary_employee = max(
    employees,
    key=lambda emp: employees[emp]["salary"]
)

print("\nEmployee with Maximum Salary:")
print("Employee ID:", highest_salary_employee)
print("Name:", employees[highest_salary_employee]["name"])
print("Department:", employees[highest_salary_employee]["department"])
print("Salary:", employees[highest_salary_employee]["salary"])

# 4. Insert a new employee record
employees["E6"] = {
    "name": "Neha",
    "department": "Sales",
    "salary": 52000
}

print("\nAfter inserting new employee:")
print(employees["E6"])
