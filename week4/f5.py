# Multi-Region Sales Analytics Engine
# Problem Statement
# You are given a list of regions. Each region contains multiple stores, and each store contains multiple transactions.
# Each transaction has:
# • amount (float)
# • category (string)
# • successful (boolean)
# Task
# • Consider only transactions that:
# • Are successful
# • Belong to category "Electronics"
# • Have amount ≥ 100
# Apply:
# • 18% GST to each valid transaction
# • Then apply an additional 5% regional surcharge
# Compute:
# • The total revenue per region
# • Then return the grand total across all regions

# Input: 
# regions = [
#     {
#         "region": "North",
#         "stores": [
#             {
#                 "transactions": [
#                     {"amount": 200, "category": "Electronics", "successful": True},
#                     {"amount": 50, "category": "Electronics", "successful": True},
#                     {"amount": 500, "category": "Clothing", "successful": True}
#                 ]
#             }
#         ]
#     },
#     {
#         "region": "South",
#         "stores": [
#             {
#                 "transactions": [
#                     {"amount": 300, "category": "Electronics", "successful": True},
#                     {"amount": 150, "category": "Electronics", "successful": False}
#                 ]
#             }
#         ]
#     }
# ]

# Final output: single float (grand total)

regions = [
    {
        "region": "North",
        "stores": [
            {
                "transactions": [
                    {"amount": 200, "category": "Electronics", "successful": True},
                    {"amount": 50, "category": "Electronics", "successful": True},
                    {"amount": 500, "category": "Clothing", "successful": True}
                ]
            }
        ]
    },
    {
        "region": "South",
        "stores": [
            {
                "transactions": [
                    {"amount": 300, "category": "Electronics", "successful": True},
                    {"amount": 150, "category": "Electronics", "successful": False}
                ]
            }
        ]
    }
]
from functools import reduce
grandTotal = reduce(lambda acc,region: acc + reduce(lambda acc2,store: acc2 + sum(map(lambda x: x*1.18*1.05,filter(lambda x: x["successful"] == True and x["category"] == "Electronics" and x["amount"] >= 100,store["transactions"])),0), region["stores"], 0), regions, 0)
print(grandTotal)