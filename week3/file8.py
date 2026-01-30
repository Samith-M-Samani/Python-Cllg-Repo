# 8. Filter Even Numbers
# Problem:
# Given a list of numbers, return a new list containing only even numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [2, 4, 6]
def checkEven(ls):
    res = []
    for i in ls:
        if i%2 == 0:
            res.append(i)
    return res
def main():
    lst = [1, 2, 3, 4, 5, 6]
    print(checkEven(lst))
if __name__ == "__main__":  
    main()