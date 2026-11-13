
# Assignment-16
# Question 1: Perform Data Analysis on Titanic Dataset using Pandas

import pandas as pd

# Load the Titanic dataset from CSV file
df = pd.read_csv("titanic.csv")

# Display original dataset
print("Original Titanic Dataset:")
print(df)

# 1. Clean the dataset
# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)

# Fill missing Fare values with median
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Fill missing Cabin values
df["Cabin"] = df["Cabin"].fillna("Unknown")

print("\nCleaned Titanic Dataset:")
print(df)

# 2. Find female passengers whose age is more than 40
print("\nFemale Passengers Above 40 Years:")

female_passengers = df[
    (df["Age"] > 40) & (df["Sex"] == "female")
]

print(female_passengers)

# 3. Describe the dataset for Pclass 1 passengers
print("\nDescription of First Class Passengers:")

first_class = df[df["Pclass"] == 1]

print(first_class.describe())

# 4. Remove duplicate values in PassengerId
df = df.drop_duplicates(subset=["PassengerId"])

print("\nDataset After Removing Duplicate PassengerId:")
print(df)

# 5. Insert a new column named FamilySize
df.insert(
    3,
    "FamilySize",
    df["SibSp"] + df["Parch"] + 1
)

print("\nDataset After Inserting FamilySize Column:")
print(df)

# Display final dataset information
print("\nFinal Dataset Information:")
print(df.info())
