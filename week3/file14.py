# 14. Character Index Map
# Problem:
# Given a string, return a dictionary mapping each character to a tuple of all its indices.
# Input:
# "banana"
# Output:
# {"b": (0,), "a": (1,3,5), "n": (2,4)}
def char_index_map(s):
    index_map = {}
    for index, char in enumerate(s):
        if char in index_map:
            index_map[char] += (index,)
        else:
            index_map[char] = (index,)
    return index_map
s = "banana"
result = char_index_map(s)
print(result)