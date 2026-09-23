# Question 3: 90% Interval of Standard Normal Distribution
#
# Find the central 90% interval of a standard normal distribution
# using SciPy.

from scipy import stats


# Confidence level
confidence_level = 0.90


# Calculate the interval
lower_limit, upper_limit = stats.norm.interval(confidence_level)


# Display results
print("===== Standard Normal Distribution Interval =====")
print("Confidence level:", confidence_level * 100, "%")
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("90% interval:", (lower_limit, upper_limit))
