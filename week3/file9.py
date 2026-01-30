# 9. Student Average Score
# Problem:
# You are given a list of tuples where each tuple contains a student name and a list of marks. Return a dictionary mapping each student’s name (lowercase) to their average score.
# Input:
# [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
# Output:
# {"alice": 85.0, "bob": 81.67}
def calcAvg(data):
    result = {}
    for name, marks in data:
        avg = sum(marks) / len(marks)
        result[name.lower()] = round(avg, 2)
    return result
def main():
    
    data = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
    print(calcAvg(data))
if __name__ == "__main__":
    main()