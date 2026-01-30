# 3. Tuple to Dictionary
# Problem:
# Given a tuple of (key, value) pairs, convert it into a dictionary.
# Input:
# (("a", 1), ("b", 2))
# Output:
# {"a": 1, "b": 2}
def main():
    tup1 = (("a",1),("b",2))
    di = dict(tup1)
    print(di)
if __name__ == "__main__":
    main() 