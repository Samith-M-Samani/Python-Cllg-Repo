# 4. Convert & Filter Product Prices

# Problem Statement
# You are given a list of tuples (product_name, price_in_dollars).
# Convert prices to INR (1 USD = 83 INR) and return only products costing more than ₹3000.

# Input

# products = [
#     ("Pen", 10),
#     ("Bag", 50),
#     ("Shoes", 60)
# ]


# Output

# [("Bag", 4150), ("Shoes", 4980)]


# Constraints

# Use map() for conversion

# Use filter() for price condition

products = [
    ("Pen", 10),
    ("Bag", 50),
    ("Shoes", 60)
    ]
converted_vals = list(map(lambda pro: pro[1]*83,products))
print(converted_vals)
filtered_vals = list(filter(lambda price: price>3000,converted_vals))
print(filtered_vals)