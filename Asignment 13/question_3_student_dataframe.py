import pandas as pd

# Create student DataFrame
data = {
    "Roll": ["01", "02", "03", "04", "05"],
    "Name": ["Ans", "Ria", "Sima", "Raju", "Binita"],
    "Department": ["CSE", "IT", None, "ECE", None],
    "Marks": [90, None, 80, 85, 95]
}

df = pd.DataFrame(data)

print("===== ORIGINAL STUDENT DATAFRAME =====")
print(df)

# 1. Find columns containing null values
print("\nColumns with null values:")
print(df.columns[df.isnull().any()].tolist())

# 2. Fill Sima's missing department with CSE
df.loc[df["Name"] == "Sima", "Department"] = "CSE"

print("\nAfter filling Sima's department:")
print(df)

# 3. Delete Binita's record
df = df[df["Name"] != "Binita"].copy()

print("\nAfter deleting Binita's record:")
print(df)

# 4. Update Raju's department to VLSI
df.loc[df["Name"] == "Raju", "Department"] = "VLSI"

print("\nFinal Student DataFrame:")
print(df.reset_index(drop=True))
