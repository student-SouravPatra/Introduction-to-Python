# Question 2: Employee DataFrame using Melt, Stack and Unstack

import pandas as pd

# Create Employee DataFrame in Wide Format
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Riya", "Sourav", "Rahul", "Priya"],
    "Kolkata": [9876543210, 9876543211, 9876543212, None, 9876543214],
    "Delhi": [9123456780, None, 9123456782, 9123456783, None],
    "Mumbai": [None, 9988776655, 9988776656, 9988776657, 9988776658]
}

df = pd.DataFrame(data)

# Display Wide Format DataFrame
print("Employee DataFrame (Wide Format):")
print(df)

# Convert Wide Format into Long Format using Melt
df_long = pd.melt(
    df,
    id_vars=["Employee_ID", "Employee_Name"],
    var_name="Project_Location",
    value_name="Contact_No"
)

# Remove missing contact numbers
df_long = df_long.dropna(subset=["Contact_No"])

print("\nEmployee DataFrame (Long Format):")
print(df_long)

# Demonstrate Stack Method
print("\nStack Method:")

stacked = df.set_index(
    ["Employee_ID", "Employee_Name"]
).stack()

print(stacked)

# Demonstrate Unstack Method
print("\nUnstack Method:")

unstacked = stacked.unstack()

print(unstacked)



#Output
Employee DataFrame (Wide Format):
   Employee_ID Employee_Name     Kolkata       Delhi      Mumbai
0          101          Amit  9876543210  9123456780         NaN
1          102          Riya  9876543211         NaN  9988776655
2          103        Sourav  9876543212  9123456782  9988776656
3          104         Rahul         NaN  9123456783  9988776657
4          105         Priya  9876543214         NaN  9988776658

Employee DataFrame (Long Format):
    Employee_ID Employee_Name Project_Location    Contact_No
0           101          Amit          Kolkata  9.876543e+09
1           102          Riya          Kolkata  9.876543e+09
2           103        Sourav          Kolkata  9.876543e+09
4           105         Priya          Kolkata  9.876543e+09
5           101          Amit            Delhi  9.123457e+09
7           103        Sourav            Delhi  9.123457e+09
8           104         Rahul            Delhi  9.123457e+09
11          102          Riya           Mumbai  9.988777e+09
12          103        Sourav           Mumbai  9.988777e+09
13          104         Rahul           Mumbai  9.988777e+09
14          105         Priya           Mumbai  9.988777e+09
