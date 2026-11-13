

# Assignment-13
# Question 1: Calculate descriptive statistics using SciPy

from scipy import stats

# Marks of 10 students
marks = [18, 16, 12, 17, 15, 19, 20, 16, 18, 15]

# Calculate descriptive statistics
res = stats.describe(marks)

# Display the result
print("Descriptive Statistics:")
print(res)


#Output:
Descriptive Statistics:
DescribeResult(
nobs=10,
minmax=(12, 20),
mean=16.6,
variance=5.3777777778,
skewness=-0.4440270473,
kurtosis=-0.2865924459
)

