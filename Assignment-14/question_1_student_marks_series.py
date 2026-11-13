# Question 1: Create a Series of marks of 5 students using Pandas

import pandas as pd

# Create a Series of student marks
marks = pd.Series(
    [50, 60, 70, 80, 90],
    index=["Student1", "Student2", "Student3", "Student4", "Student5"]
)

# Display the Series
print("Marks of 5 Students:")
print(marks)


#Output:
Marks of 5 Students:
Student1    50
Student2    60
Student3    70
Student4    80
Student5    90
dtype: int64
