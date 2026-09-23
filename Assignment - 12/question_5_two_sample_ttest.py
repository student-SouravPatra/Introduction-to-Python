# Question 5: Independent Two-Sample t-Test
#
# Compare the means of two independent groups
# using an independent two-sample t-test.

import numpy as np
from scipy import stats


# Given data
marks_b = np.array([12, 17, 16, 14])
marks_g = np.array([18, 17, 16, 20, 19])

# Significance level
alpha = 0.05


# Perform independent two-sample t-test
# equal_var=False performs Welch's t-test
t_statistic, p_value = stats.ttest_ind(
    marks_b,
    marks_g,
    equal_var=False
)


# Display results
print("===== Independent Two-Sample t-Test =====")
print("Group B:", marks_b)
print("Group G:", marks_g)
print()

print("Mean of Group B:", np.mean(marks_b))
print("Mean of Group G:", np.mean(marks_g))
print()

print("t-statistic:", t_statistic)
print("p-value:", p_value)
print("Significance level:", alpha)
print()


# Hypothesis testing decision
if p_value < alpha:
    print("Decision: Reject H0")
    print("Conclusion: The two group means are significantly different.")
else:
    print("Decision: Fail to reject H0")




  # Output
  ===== Independent Two-Sample t-Test =====
Group B: [12 17 16 14]
Group G: [18 17 16 20 19]

Mean of Group B: 14.75
Mean of Group G: 18.0

t-statistic: -2.4715
p-value: 0.0538
Significance level: 0.05

Decision: Fail to reject H0
Conclusion: There is not enough evidence to conclude that the two group means are significantly different.
    print("Conclusion: There is not enough evidence to conclude that the two group means are significantly different.")
