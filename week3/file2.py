# 2. Dictionary Key Check
# Problem:
# Given a dictionary and a key, return "Found" if the key exists, otherwise return "Not Found".
# Input:
# {"a": 1, "b": 2}, key = "b"
# Output:
# "Found"
def check(dct, key):
    if key in dct:
        return "Found"
    else:
        return "Not Found"
def main():
    dctt = {"a": 1, "b": 2}
    k = "b"
    result = check(dctt, k)
    print(result)
if __name__ == "__main__":
    main()