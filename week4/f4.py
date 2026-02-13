# 3. Student Weighted Score Calculator
# Problem Statement
# You are given a list of students:

# Task:
# • Keep students whose average is ≥ 60
# • Increase each mark by 5 grace marks
# • Compute the total of all updated marks
# Input
# students = [
#     {"name": "A", "marks": [50, 60, 70]},
#     {"name": "B", "marks": [30, 40]},
#     {"name": "C", "marks": [80, 90]}
# ]

# Output: 
# 375
students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]
from functools import reduce
totalMarks = reduce(lambda acc,student: acc + sum(map(lambda x: x+5,student["marks"])) if sum(student["marks"])/len(student["marks"]) >= 60 else acc, students, 0)
print(totalMarks)