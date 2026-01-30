# 5. Sum of Tuples
# Problem:
# Given a list of tuples containing two integers each, return a list of their sums.
# Input:
# [(1, 2), (3, 4), (5, 6)]
# Output:
# [3, 7, 11]
def main():
    tuple_list = [(1, 2), (3, 4), (5, 6)]
    sum_list = [a + b for a, b in tuple_list]
    print(sum_list)
if __name__ == "__main__":
    main()