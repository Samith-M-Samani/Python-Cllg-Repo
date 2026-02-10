# 1. Average Salary Excluding Min and Max (Using Map & Filter)
# Problem Statement
# You are given a list of dictionaries where each dictionary represents an employee with name and salary.
# Remove the employees with the minimum and maximum salary, then return the average salary of the remaining employees.
# Input
# employees = [
#     {"name": "A", "salary": 30000},
#     {"name": "B", "salary": 50000},
#     {"name": "C", "salary": 40000},
#     {"name": "D", "salary": 60000}
# ]
# Output
# 40000.0
# Constraints
# Use map() and filter()
# Do not use explicit loops
def average_salary_excluding_min_max(employees):
    
    salaries = list(map(lambda emp: emp['salary'], employees))
    
    
    min_salary = min(salaries)
    max_salary = max(salaries)
    
    
    filtered_employees = list(filter(lambda emp: emp['salary'] != min_salary and emp['salary'] != max_salary, employees))
    
    
    if len(filtered_employees) == 0:
        return 0  
    
    total_salary = sum(map(lambda emp: emp['salary'], filtered_employees))
    average_salary = total_salary / len(filtered_employees)
    
    return average_salary