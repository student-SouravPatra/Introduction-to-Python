# Question 5: Perform an independent two-sample t-test

from scipy import stats

# Marks of two groups
marks_b = [12, 17, 16, 13, 14]
marks_g = [18, 17, 16, 20, 19]

# Perform independent t-test
t, p = stats.ttest_ind(marks_b, marks_g)

print("T-statistic:", t)
print("P-value:", p)

# Check the hypothesis
if p < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")


#Output:
T-statistic: -3.0869745325651583
P-value: 0.014957960244786466
Reject the null hypothesis.
