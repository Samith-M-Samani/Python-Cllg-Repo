def greet(name):
    print("Hello,", name)
def add(a, b):
    return a + b
def power(base, exponent=2):
    return base ** exponent
def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Not possible")
greet("Krish")
result = add(10, 5)
print("Sum:", result)
print("Power:", power(4)) 
calculator(8, 2)