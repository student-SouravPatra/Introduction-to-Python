# Question 4: One-Sample t-Test
#
# Perform a one-sample t-test on the given sample
# against a population mean of 50 using SciPy.

import numpy as np
from scipy import stats


# Given sample data
marks = np.array([18, 15, 12, 20, 17])

# Given population mean
population_mean = 50

# Significance level
alpha = 0.05


# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(
    marks,
    population_mean
)


# Display results
print("===== One-Sample t-Test =====")
print("Sample data:", marks)
print("Population mean:", population_mean)
print("Significance level:", alpha)
print()

print("t-statistic:", t_statistic)
print("p-value:", p_value)
print()


# Hypothesis testing decision
if p_value < alpha:
    print("Decision: Reject H0")
    print("Conclusion: The sample mean is significantly different from the population mean.")
else:
    print("Decision: Fail to reject H0")
    print("Conclusion: There is not enough evidence to say that the sample mean differs from the population mean.")



#Output
===== One-Sample t-Test =====
Sample data: [18 15 12 20 17]
Population mean: 50
Significance level: 0.05

t-statistic: -24.6367
p-value: 1.61e-05

Decision: Reject H0
Conclusion: The sample mean is significantly different from the population mean.
