```python
# Assignment-14
# Question 1: Write a Python program using Pandas to create a Series
# from a list, assign custom index labels, access elements by index,
# display the first three elements, calculate statistical summaries,
# and find the mean, maximum, and minimum values.

import pandas as pd

# Create a Pandas Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Pandas Series:")
print(series)

# Create a Series with custom index labels
custom_series = pd.Series(
    [85, 90, 78, 92, 88],
    index=["Alice", "Bob", "Charlie", "David", "Emma"]
)

print("\nSeries with Custom Index:")
print(custom_series)

# Access an element by index label
print("\nMarks of Alice:")
print(custom_series["Alice"])

# Display the first three elements
print("\nFirst Three Elements:")
print(custom_series.head(3))

# Display basic statistical information
print("\nStatistical Summary:")
print(custom_series.describe())

# Calculate the mean
print("\nAverage Marks:")
print(custom_series.mean())

# Calculate the maximum and minimum
print("\nMaximum Marks:", custom_series.max())
print("Minimum Marks:", custom_series.min())
```
