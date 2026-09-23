# Question 6: Chi-Square Test of Independence
#
# Perform a Chi-Square Test of Independence using SciPy.
#
# H0: The two categorical variables are independent.
# H1: The two categorical variables are associated.

import numpy as np
from scipy import stats


# Contingency table
#
# Rows    -> Groups
# Columns -> Categories
observed = np.array([
    [12, 17, 16, 14],
    [18, 17, 16, 20]
])


# Significance level
alpha = 0.05


# Perform Chi-Square Test of Independence
chi_square, p_value, degrees_of_freedom, expected = (
    stats.chi2_contingency(observed)
)


# Display results
print("===== Chi-Square Test of Independence =====")
print("Observed Frequencies:")
print(observed)
print()

print("Chi-square statistic:", chi_square)
print("p-value:", p_value)
print("Degrees of freedom:", degrees_of_freedom)
print()

print("Expected Frequencies:")
print(expected)
print()


# Hypothesis testing decision
if p_value < alpha:
    print("Decision: Reject H0")
    print(
        "Conclusion: There is a statistically significant "
        "association between the categorical variables."
    )
else:
    print("Decision: Fail to reject H0")
    print(
        "Conclusion: There is not enough evidence to conclude "
        "that the categorical variables are associated."




      # Output
    ===== Chi-Square Test of Independence =====
Observed Frequencies:
[[12 17 16 14]
 [18 17 16 20]]

Chi-square statistic: 1.161...
p-value: 0.762...
Degrees of freedom: 3

Expected Frequencies:
[[14.11764706 16.         15.05882353 13.82352941]
 [15.88235294 18.         16.94117647 20.17647059]]

Decision: Fail to reject H0
Conclusion: There is not enough evidence to conclude that the categorical variables are associated.  
    )
