# Question 2: Calculate normal distribution probability using SciPy

from scipy import stats

# Calculate probability that Z is less than 1.5
p = stats.norm.cdf(1.5)

print("Probability that Z is less than 1.5:")
print(p)


#Output:
Probability that Z is less than 1.5:
0.9331927987311419
