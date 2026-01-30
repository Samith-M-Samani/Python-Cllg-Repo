# 12. Unique Values Extractor
# Problem:
# Given a dictionary where keys are strings and values are lists of integers, return a sorted list of all unique integers across all lists.
# Input:
# {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
# Output:
# [1, 2, 3, 4, 5]\
    
def main():
    data = {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
    result = sorted({v for values in data.values() for v in values})

    print(result)
if __name__ == "__main__":
    main()