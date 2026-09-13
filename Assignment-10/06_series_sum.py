import math

n = int(input("Enter the number of terms: "))

total = 0

for i in range(1, n + 1):
    total += (i ** 2) / math.factorial(i)

print("Sum of the series:", total)
