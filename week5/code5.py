def charCountRep(s):
    char_count = {}
    for char in s:
        if len(char) in char_count:
            char_count[len(char)].append(char)
        else:
            char_count[len(char)] = [char]
    return char_count
strr = ['a', 'bb', 'cde', 'dd', 'eee']
print(charCountRep(strr))