customers = [
    ("Amit", 8000),
    ("Neha", 15000),
    ("Rahul", 12000),
    ("Priya", 5000),
    ("Karan", 20000)
]
print("All Customers:")
for customer in customers:
    print(customer)
premium_customers = list(filter(lambda c: c[1] > 10000, customers))
print("\nPremium Customers (Balance > 10000):")
for customer in premium_customers:
    print("Name:", customer[0], "| Balance:", customer[1])
