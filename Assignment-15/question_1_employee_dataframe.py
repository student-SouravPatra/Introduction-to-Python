# Question 1: Create an Employee DataFrame using Dictionary

import pandas as pd

# Create a dictionary containing employee details
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Riya", "Sima", "Raju", "Binta"],
    "Department_Name": ["HR", "IT", "Finance", "Sales", "IT"],
    "Salary": [30000, 45000, 35000, 50000, 60000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the complete DataFrame
print("Employee DataFrame:")
print(df)

# 1. Print the first two employee records
print("\nFirst Two Employee Records:")
print(df.head(2))

# 2. Print the last two employee records
print("\nLast Two Employee Records:")
print(df.tail(2))

# 3. Print the employee having maximum salary
print("\nEmployee Having Maximum Salary:")
print(df[df["Salary"] == df["Salary"].max()])




#Output:
Employee DataFrame:
   Employee_ID Employee_Name Department_Name  Salary
0          101          Amit              HR   30000
1          102          Riya              IT   45000
2          103          Sima         Finance   35000
3          104          Raju           Sales   50000
4          105         Binta              IT   60000

First Two Employee Records:
   Employee_ID Employee_Name Department_Name  Salary
0          101          Amit              HR   30000
1          102          Riya              IT   45000

Last Two Employee Records:
   Employee_ID Employee_Name Department_Name  Salary
3          104          Raju           Sales   50000
4          105         Binta              IT   60000

Employee Having Maximum Salary:
   Employee_ID Employee_Name Department_Name  Salary
4          105         Binta              IT   60000



