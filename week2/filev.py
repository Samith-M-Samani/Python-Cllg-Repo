# permutations of a list
def permute(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in len(lst):
        sub = lst[:i] + lst[i+1:]
        for ele in sub:
            00
    return result
# lst = [1,4,2]
# print(lst[:1] + lst[1+1:])
