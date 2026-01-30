# 4. Reverse Words
# Problem:
# Given a string, return a list of words in reverse order.
# Input:
# "data science is fun"
# Output:
# ["fun", "is", "science", "data"]
def main():
    stt = "data science is fun"
    lst = stt.split(" ")
    lst.reverse()
    print(lst)
if __name__ == "__main__":
    main()