# Question 7: Pandas Series
#
# This program demonstrates:
# 1. Creating a Pandas Series of student marks
# 2. Creating a Pandas Series of grocery products and prices
# 3. Performing operations on the Series

import pandas as pd


# ============================================================
# PART A: Create a Series of Marks of 5 Students
# ============================================================

marks = pd.Series(
    [18, 17, 13, 12, 20],
    index=["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"]
)

print("========== PART A: STUDENT MARKS ==========")
print(marks)
print()


# ============================================================
# PART B: Grocery Product Price Series
# ============================================================

# Create a Series of 10 grocery products with their prices
products = pd.Series(
    [30, 60, 70, 80, 90, 45, 55, 40, 75, 100],
    index=[
        "Rice",
        "Sugar",
        "Oil",
        "Dal",
        "Biscuits",
        "Salt",
        "Tea",
        "Flour",
        "Soap",
        "Coffee"
    ]
)


print("========== PART B: GROCERY PRODUCTS ==========")
print(products)
print()


# ------------------------------------------------------------
# 1. Print the products with their prices
# ------------------------------------------------------------

print("1. Products with their prices:")
print(products)
print()


# ------------------------------------------------------------
# 2. Find the average price of the products
# ------------------------------------------------------------

average_price = products.mean()

print("2. Average price of products:")
print(average_price)
print()


# ------------------------------------------------------------
# 3. Print the names and prices of products whose
#    price is more than the average price
# ------------------------------------------------------------

above_average = products[products > average_price]

print("3. Products whose price is more than the average price:")
print(above_average)
print()


# ------------------------------------------------------------
# 4. List the names of products whose price is
#    more than 50 rupees
# ------------------------------------------------------------

products_above_50 = products[products > 50]

print("4. Products whose price is more than Rs. 50:")
print(products_above_50)
print()


# ------------------------------------------------------------
# Display only product names for price > Rs. 50
# ------------------------------------------------------------

print("Product names with price more than Rs. 50:")
print(products[products > 50].index.tolist())







# Output
========== PART A: STUDENT MARKS ==========
Student 1    18
Student 2    17
Student 3    13
Student 4    12
Student 5    20
dtype: int64


========== PART B: GROCERY PRODUCTS ==========
Rice         30
Sugar        60
Oil          70
Dal          80
Biscuits     90
Salt         45
Tea          55
Flour        40
Soap         75
Coffee      100
dtype: int64


1. Products with their prices:
Rice         30
Sugar        60
Oil          70
Dal          80
Biscuits     90
Salt         45
Tea          55
Flour        40
Soap         75
Coffee      100
dtype: int64


2. Average price of products:
64.5


3. Products whose price is more than the average price:
Oil         70
Dal         80
Biscuits    90
Soap        75
Coffee     100
dtype: int64


4. Products whose price is more than Rs. 50:
Sugar       60
Oil         70
Dal         80
Biscuits    90
Tea         55
Soap        75
Coffee     100
dtype: int64

Product names with price more than Rs. 50:
['Sugar', 'Oil', 'Dal', 'Biscuits', 'Tea', 'Soap', 'Coffee']


products = pd.Series(
    [30, 60, 70, 80, 90, 45, 55, 40, 75, 100],
    index=[
        "Rice",
        "Sugar",
        "Oil",
        "Dal",
        "Biscuits",
        "Salt",
        "Tea",
        "Flour",
        "Soap",
        "Coffee"
    ]
)
