# 3. Students Passed All Subjects

# Problem Statement
# You are given a dictionary where keys are student names and values are lists of marks.
# Return a list of student names who scored 40 or above in all subjects.

# Input

# students = {
#     "Alice": [45, 50, 60],
#     "Bob": [35, 55, 65],
#     "Charlie": [40, 40, 40]
# }


# Output

# ["Alice", "Charlie"]


# Constraints

# Use filter() on dictionary items

# Use map() to extract names
def students_passed_all_subjects(students):
    
    passed_students = list(filter(lambda item: all(mark >= 40 for mark in item[1]), students.items()))
    
    student_names = list(map(lambda item: item[0], passed_students))
    
    return student_names