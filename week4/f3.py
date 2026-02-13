# 2. Problem Statement
# You are given a list of products as tuples:

#  Task:
# • Keep only products in category "Electronics"
# • Apply a 20% discount
# • Return the total discounted price
# Input
# products = [
#     ("Laptop", "Electronics", 1000),
#     ("Shirt", "Clothing", 50),
#     ("Phone", "Electronics", 500)
# ]
# Output:
# 1200.0
from functools import reduce
products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
totalRes = reduce(lambda acc,product: acc + product[2]*0.8 if product[1] == "Electronics" else acc, products, 0)
print(totalRes)