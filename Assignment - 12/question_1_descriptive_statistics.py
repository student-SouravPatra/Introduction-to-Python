# Question 1: Descriptive Statistics using SciPy
#
# Calculate descriptive statistics for the given dataset
# using scipy.stats.describe().
#
# Dataset:
# [18, 16, 12, 14, 13, 19, 20, 16, 18, 15]

import numpy as np
from scipy import stats


# Given dataset
marks = np.array([18, 16, 12, 14, 13, 19, 20, 16, 18, 15])


# Calculate descriptive statistics
result = stats.describe(marks)


# Display results
print("===== Descriptive Statistics =====")
print("Dataset:", marks)
print()

print("Number of observations:", result.nobs)
print("Minimum value:", result.minmax[0])
print("Maximum value:", result.minmax[1])
print("Mean:", result.mean)
print("Variance:", result.variance)
print("Skewness:", result.skewness)
print("Kurtosis:", result.kurtosis)
