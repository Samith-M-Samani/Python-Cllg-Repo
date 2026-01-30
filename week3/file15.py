# 15. Dictionary Value Merger
# Problem:
# Given a list of dictionaries with integer values, merge them into a single dictionary by summing values of common keys.
# Input:
# [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
# Output:
# {"a": 6, "b": 3, "c": 1}
dict_list = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
merged_dict = {}
# merged_dict = {k: sum(d.get(k, 0) for d in dict_list) for k in set().union(*dict_list)}

for d in dict_list:
    for key, value in d.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
print(merged_dict)