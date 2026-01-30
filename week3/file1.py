# 1. Count Elements
# Problem:
# Given a list of integers, return a dictionary with each number and its count.
# Input:
# [1, 2, 2, 3, 3, 3]
# Output:
# {1: 1, 2: 2, 3: 3}
def count_elements(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
def main():
    lls = [1, 2, 2, 3, 3, 3]
    result = count_elements(lls)
    print(result) 

if __name__ == "__main__":
    main() 