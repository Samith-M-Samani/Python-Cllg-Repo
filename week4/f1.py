wprds = ["  PYTHON  ", " AI  ", "     MACHINE ", " DATA "]
def op(word):
    return word.strip().lower()
meow  = map(lambda word: word.strip().lower(),wprds)
print(list(filter(lambda x: len(x)>= 5 ,meow)))