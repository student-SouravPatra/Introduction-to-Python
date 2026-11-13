# Question 2: Create a Series of 10 grocery products with prices

import pandas as pd

# Create a Series of grocery products and their prices
products = pd.Series(
    [60, 30, 25, 70, 45, 120, 80, 20, 40, 55],
    index=["Rice", "Milk", "Bread", "Eggs", "Sugar",
           "Oil", "Tea", "Salt", "Biscuits", "Soap"]
)

# 1. Display product names and prices
print("Grocery Products and Their Prices:")
print(products)

# 2. Calculate the average price
avg_price = products.mean()

print("\nAverage Price of Products:")
print(avg_price)

# 3. Display products whose price is greater than average
print("\nProducts with Price Greater Than Average:")
print(products[products > avg_price])

# 4. Display product names whose price is greater than 50
print("\nProducts Whose Price is More Than 50 Rupees:")
print(products[products > 50].index.tolist())



#Output
Grocery Products and Their Prices:
Rice        60
Milk        30
Bread       25
Eggs        70
Sugar       45
Oil        120
Tea         80
Salt        20
Biscuits    40
Soap        55
dtype: int64

Average Price of Products:
54.5

Products with Price Greater Than Average:
Rice     60
Eggs     70
Oil     120
Tea      80
Soap     55
dtype: int64

Products Whose Price is More Than 50 Rupees:
['Rice', 'Eggs', 'Oil', 'Tea', 'Soap']
