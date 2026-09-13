# Assignment 4 - Program 1
# Fruit Sets

# Set of 10 fruits
fruits = {
    "apple",
    "banana",
    "orange",
    "mango",
    "pineapple",
    "grapes",
    "watermelon",
    "papaya",
    "guava",
    "strawberry"
}

# Summer fruits
summer_fruits = {
    "mango",
    "watermelon",
    "papaya",
    "orange",
    "guava"
}

# Winter fruits
winter_fruits = {
    "apple",
    "orange",
    "grapes",
    "strawberry",
    "pineapple"
}

# 1. Print all fruits in the three sets
print("Fruits:", fruits)
print("Summer Fruits:", summer_fruits)
print("Winter Fruits:", winter_fruits)

# 2. Fruits present in both fruits and winter fruits
common_fruits = fruits.intersection(winter_fruits)
print("\nFruits present in both fruits and winter fruits:")
print(common_fruits)

# 3. Summer fruits but not in fruits
summer_not_in_fruits = summer_fruits.difference(fruits)
print("\nSummer fruits not present in fruits:")
print(summer_not_in_fruits)

# 4. Fruits present in both summer and winter but not in fruits
summer_and_winter = summer_fruits.intersection(winter_fruits)
result = summer_and_winter.difference(fruits)

print("\nFruits present in both summer and winter but not in fruits:")
print(result)

# 5. Check whether orange is present in fruits
if "orange" in fruits:
    print("\nOrange is present in the fruits set.")
else:
    print("\nOrange is not present in the fruits set.")

# 6. Find in which set pineapple is present
print("\nPineapple is present in:")

if "pineapple" in fruits:
    print("- Fruits set")

if "pineapple" in summer_fruits:
    print("- Summer fruits set")

if "pineapple" in winter_fruits:
    print("- Winter fruits set")
