#longest word in a string
def wordLen(s):
    words = s.split()
    longest = ""
    liss = []
    for word in words:
        if len(word) > len(longest):
            longest = word
    for word in words:
        if len(word) > len(longest):
            liss.append(word)
    return longest
strr = "The morning sun spilled gold across the quiet harbor. She closed the book, knowing some stories linger long after the final page."
print(wordLen(strr))