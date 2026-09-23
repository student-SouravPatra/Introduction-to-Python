#Create a DataFrame using a dictionary for five employees with Employee ID, Employee Name, Department and Salary. 
#Then display the first two employees, last two employees and the employee with the maximum salary.

import pandas as pd

# Create employee DataFrame
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohit"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales"],
    "Salary": [45000, 55000, 60000, 50000, 70000]
}

df = pd.DataFrame(data)

print("===== EMPLOYEE DATAFRAME =====")
print(df)

# 1. Display the first two employees
print("\nFirst two employees:")
print(df.head(2))

# 2. Display the last two employees
print("\nLast two employees:")
print(df.tail(2))

# 3. Display the employee with maximum salary
print("\nEmployee with maximum salary:")
print(df.loc[df["Salary"].idxmax()])
