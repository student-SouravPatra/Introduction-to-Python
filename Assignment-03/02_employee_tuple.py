# Assignment 3 - Program 2
# Employee Names using Tuple

# Tuple of 20 employee names
employees = (
    "Rahul",
    "Amit",
    "Priya",
    "Sneha",
    "Rahul",
    "Rohan",
    "Amit",
    "Neha",
    "Suman",
    "Priya",
    "Arjun",
    "Rahul",
    "Sneha",
    "Riya",
    "Amit",
    "Karan",
    "Neha",
    "Rahul",
    "Rohan",
    "Priya"
)

# 1. Print each employee name and its frequency
print("Employee Names and Frequencies:")

for name in employees:
    if employees.index(name) == employees.index(name):
        print(name, ":", employees.count(name))

# 2. Remove duplicate items and find distinct names
distinct_names = tuple(dict.fromkeys(employees))

print("\nDistinct Employee Names:")
print(distinct_names)

# 3. Find the employee name having maximum frequency
max_frequency = 0
most_frequent_employee = ""

for name in distinct_names:
    frequency = employees.count(name)

    if frequency > max_frequency:
        max_frequency = frequency
        most_frequent_employee = name

print("\nEmployee with Maximum Frequency:")
print(most_frequent_employee)
print("Frequency:", max_frequency)

# 4. Sort the tuple alphabetically
sorted_employees = tuple(sorted(employees))

print("\nEmployees in Alphabetical Order:")
print(sorted_employees)

# 5. Check whether a specific employee exists
search_name = input("\nEnter employee name to search: ")

if search_name in employees:
    print(search_name, "exists in the tuple.")
else:
    print(search_name, "does not exist in the tuple.")
