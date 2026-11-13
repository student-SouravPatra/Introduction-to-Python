# Question 2: Create a Student DataFrame and Handle Missing Values

import pandas as pd

# Create a dictionary containing student details
data = {
    "Roll_No": [1, 2, 3, 4, 5],
    "Name": ["Ans", "Ria", "Sima", "Raju", "Binta"],
    "Dept": ["CSE", "IT", None, "ECL", None],
    "Marks": [90, 75, 80, 85, 95]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original Student DataFrame:")
print(df)

# 1. Find columns containing null values
print("\nColumns Containing Null Values:")
print(df.columns[df.isnull().any()].tolist())

# 2. Fill the null value of Sima with CSE
df.loc[df["Name"] == "Sima", "Dept"] = "CSE"

print("\nAfter Filling Sima's Department:")
print(df)

# 3. Delete the record containing the null value of Binta
df = df.dropna(subset=["Dept"])

print("\nAfter Deleting Binta's Null Record:")
print(df)

# 4. Update the department of Raju with VLSI
df.loc[df["Name"] == "Raju", "Dept"] = "VLSI"

print("\nAfter Updating Raju's Department:")
print(df)




#Output
Original Student DataFrame:
   Roll_No   Name  Dept  Marks
0        1    Ans   CSE     90
1        2    Ria    IT     75
2        3   Sima  None     80
3        4   Raju   ECL     85
4        5  Binta  None     95

Columns Containing Null Values:
['Dept']

After Filling Sima's Department:
   Roll_No   Name  Dept  Marks
0        1    Ans   CSE     90
1        2    Ria    IT     75
2        3   Sima   CSE     80
3        4   Raju   ECL     85
4        5  Binta  None     95

After Deleting Binta's Null Record:
   Roll_No  Name Dept  Marks
0        1   Ans  CSE     90
1        2   Ria   IT     75
2        3  Sima  CSE     80
3        4  Raju  ECL     85

After Updating Raju's Department:
   Roll_No  Name  Dept  Marks
0        1   Ans   CSE     90
1        2   Ria    IT     75
2        3  Sima   CSE     80
3        4  Raju  VLSI     85
