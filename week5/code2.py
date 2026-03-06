
def are_rotations(a, b):
    if len(a) != len(b):
        return False
    return a in b + b
a = "abcd"
b = "cdab"
print(are_rotations(a, b))