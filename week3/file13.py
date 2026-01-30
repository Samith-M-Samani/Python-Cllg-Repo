# 13. Attendance Percentage
# Problem:
# Given a dictionary mapping employee names to a list of attendance strings ("P" or "A"), return a dictionary of employee names and their attendance percentage.
# Input:
# {"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
# Output:
# {"Ravi": 66.67, "Neha": 100.0}
attendance_data = {"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
attendance_percentage = {}
for name, records in attendance_data.items():
    total_days = len(records)
    present_days = records.count("P")
    percentage = (present_days / total_days) * 100
    attendance_percentage[name] = round(percentage, 2)
print(attendance_percentage)