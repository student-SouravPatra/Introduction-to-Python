# Question 4: Perform a one-sample t-test using SciPy

from scipy import stats

# Given marks dataset
marks = [18, 15, 12, 20, 17]

# Perform one-sample t-test
t, p = stats.ttest_1samp(marks, 50)

print("T-statistic:", t)
print("P-value:", p)

# Check the hypothesis
if p < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")


#Output:
T-statistic: -24.636715323587353
P-value: 1.6108864483174633e-05
Reject the null hypothesis.
