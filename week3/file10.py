# 10. Word Frequency Counter
# Problem:
# Given a string sentence, return a dictionary containing the frequency of each word, ignoring case and punctuation.
# Input:
# "Python is great and Python is easy"
# Output:
# {"python": 2, "is": 2, "great": 1, "and": 1, "easy": 1}
def wordFreq(str):
    lst = str.lower().split()
    freq = {}
    for word in lst:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
def main():
    str = "Python is great and Python is easy"
    print(wordFreq(str))
if __name__ == "__main__":
    main()