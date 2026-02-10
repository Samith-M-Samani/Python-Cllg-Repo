1. Average Salary Excluding Min and Max (Using Map & Filter)

Problem Statement
You are given a list of dictionaries where each dictionary represents an employee with name and salary.

Remove the employees with the minimum and maximum salary, then return the average salary of the remaining employees.

Input

employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]


Output

40000.0


Constraints

Use map() and filter()

Do not use explicit loops

2. Filter Valid Email Domains

Problem Statement
You are given a list of email addresses. Return a list of usernames (part before @) whose email domain belongs to a given set of allowed domains.

Input

emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
allowed_domains = {"gmail.com"}


Output

["alice", "carol"]


Constraints

Use filter() to validate domains

Use map() to extract usernames

3. Students Passed All Subjects

Problem Statement
You are given a dictionary where keys are student names and values are lists of marks.
Return a list of student names who scored 40 or above in all subjects.

Input

students = {
    "Alice": [45, 50, 60],
    "Bob": [35, 55, 65],
    "Charlie": [40, 40, 40]
}


Output

["Alice", "Charlie"]


Constraints

Use filter() on dictionary items

Use map() to extract names

4. Convert & Filter Product Prices

Problem Statement
You are given a list of tuples (product_name, price_in_dollars).
Convert prices to INR (1 USD = 83 INR) and return only products costing more than ₹3000.

Input

products = [
    ("Pen", 10),
    ("Bag", 50),
    ("Shoes", 60)
]


Output

[("Bag", 4150), ("Shoes", 4980)]


Constraints

Use map() for conversion

Use filter() for price condition

5. Active Users with Prime IDs

Problem Statement
You are given a list of user objects represented as dictionaries.
Return names of users who are active and whose user_id is a prime number.

Input

users = [
    {"name": "A", "user_id": 2, "active": True},
    {"name": "B", "user_id": 4, "active": True},
    {"name": "C", "user_id": 5, "active": False},
    {"name": "D", "user_id": 7, "active": True}
]


Output

["A", "D"]


Constraints

Use filter() for active + prime check

Use map() to extract names

6. Normalize and Filter Strings

Problem Statement
You are given a list of strings with mixed casing and spaces.
Normalize them (lowercase & trimmed) and return only strings with length ≥ 5.

Input

words = ["  Python ", " AI ", "Machine ", " Data "]


Output

["python", "machine"]


Constraints

Use map() for normalization