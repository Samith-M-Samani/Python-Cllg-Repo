# set1 = set(map(int, input("Enter elements of Set 1 separated by space: ").split()))
# set2 = set(map(int, input("Enter elements of Set 2 separated by space: ").split()))
# print("\nSet 1:", set1)
# print("Set 2:", set2)
# # Union
# print("\nUnion (set1 | set2):", set1 | set2)
# # Intersection
# print("Intersection (set1 & set2):", set1 & set2)
# # Difference
# print("Difference (set1 - set2):", set1 - set2)
# print("Difference (set2 - set1):", set2 - set1)
# # Symmetric Difference
# print("Symmetric Difference (set1 ^ set2):", set1 ^ set2)1
# Define a normal function
# Define a normal function
import math
num = float(input("Enter a number: "))
if num >= 0:
    result = math.sqrt(num)
    print("Square root of", num, "is", result)
else:
    print("Square root is not defined for negative numbers.")
