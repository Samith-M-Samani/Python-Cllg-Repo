# 7. Unique Characters
# Problem:
# Given a string, return a tuple of unique characters in the order they appear.
# Input:
# "programming"
# Output:
# ("p", "r", "o", "g", "a", "m", "i", "n")
def main():
    st = input("Enter String: ")
    unique_chars = []
    for char in st:
        if char not in unique_chars:
            unique_chars.append(char)
    result = tuple(unique_chars)
    print(result)
if __name__ == "__main__":  
    main()