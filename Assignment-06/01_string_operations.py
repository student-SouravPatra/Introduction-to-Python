# Assignment 6 - String Operations

text = "Python Programming"

# 1. Display "Python"
print("1. Python")

# 2. Display "Programming"
print("2. Programming")

# 3. Check whether "Java" is present.
# If not, include "Java" between "Python" and "Programming".
if "Java" not in text:
    text = "Python Java Programming"

print("3. New String:", text)

# 4. Find the length of the new string
print("4. Length of new string:", len(text))

# 5. Count the number of words in the string
word_count = len(text.split())
print("5. Number of words:", word_count)

# 6. Capitalize each word in the string
capitalized_text = text.title()
print("6. Capitalized string:", capitalized_text)

# 7. Remove all spaces from the string
no_spaces = text.replace(" ", "")
print("7. String without spaces:", no_spaces)

# 8. Print the frequency of A, P, N and M in capital letters
uppercase_text = text.upper()

print("8. Character frequencies:")

for char in ["A", "P", "N", "M"]:
    print(char, ":", uppercase_text.count(char))
