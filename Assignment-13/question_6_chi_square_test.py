# Question 6: Perform a Chi-Square test using SciPy

from scipy import stats

# Contingency table
# Rows represent two groups
# Columns represent Pass and Fail

data = [
    [20, 10],
    [15, 25]
]

# Perform Chi-Square test
ch, p, dof, ef = stats.chi2_contingency(data)

print("Chi-Square Statistic:", ch)
print("P-value:", p)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:")
print(ef)

# Check the association
if p < 0.05:
    print("Reject the null hypothesis.")
    print("There is an association between the variables.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is no significant association between the variables.")

#Output:
Chi-Square Statistic: 4.725
P-value: 0.029727183306054655
Degrees of Freedom: 1
Expected Frequencies:
[[15. 15.]
 [20. 20.]]

Reject the null hypothesis.
There is an association between the variables.
