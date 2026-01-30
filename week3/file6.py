# 6. String Length Map
# Problem:
# Given a list of strings, return a dictionary with each string and its length.
# Input:
# ["python", "ml", "ai"]
# Output:
# {"python": 6, "ml": 2, "ai": 2}
def lenMap(strs):
    return {s: len(s) for s in strs}
def main():
    str_list = ["python", "ml", "ai"]
    length_map = lenMap(str_list)
    print(length_map)
if __name__ == "__main__":
    main()