# Question 1: Convert Long Format to Wide Format using Pivot

import pandas as pd

# Create a DataFrame in long format
data = {
    "name": ["Amit", "Amit", "Riya", "Riya", "Sourav", "Sourav"],
    "subject": ["Python", "Java", "Python", "Java", "Python", "Java"],
    "marks": [85, 90, 92, 88, 95, 89]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame (Long Format):")
print(df)

# Convert long format into wide format
df_wide = df.pivot(
    index="name",
    columns="subject",
    values="marks"
)

# Display the wide format DataFrame
print("\nDataFrame in Wide Format:")
print(df_wide)
