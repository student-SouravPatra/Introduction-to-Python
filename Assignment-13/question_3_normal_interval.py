
# Assignment-13
# Question 3: Find the interval of a standard normal distribution

from scipy import stats

# Calculate 90% confidence interval
interval = stats.norm.interval(0.90)

print("90% Confidence Interval:")
print(interval)


#Output:
90% Confidence Interval:
(-1.6448536269514729, 1.6448536269514722)
