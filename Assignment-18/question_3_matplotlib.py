# Question 3: Data Visualization using Matplotlib

import matplotlib.pyplot as plt

# Subject names
subjects = ["Python", "DBMS", "Network", "Statistics"]

# Marks of two students
marks_A = [20, 25, 22, 21]
marks_B = [18, 23, 25, 24]

# Create a line plot for Student A
plt.plot(
    subjects,
    marks_A,
    marker='o',
    label="Student A"
)

# Create a line plot for Student B
plt.plot(
    subjects,
    marks_B,
    marker='s',
    label="Student B"
)

# Add chart title and labels
plt.title("Comparison of Marks of Two Students")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display legend
plt.legend()

# Display grid
plt.grid(True)

# Display the chart
plt.show()


