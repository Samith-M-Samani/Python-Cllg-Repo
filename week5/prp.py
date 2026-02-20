from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
print("Original List:", numbers)
squared = list(map(lambda x: x * x, numbers))
print("After map (Square):", squared)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("After filter (Even numbers):", even_numbers)
add = lambda a, b: a + b
print("Lambda Example (5 + 3):", add(5, 3))
total = reduce(lambda x, y: x + y, numbers)
print("After reduce (Sum):", total)