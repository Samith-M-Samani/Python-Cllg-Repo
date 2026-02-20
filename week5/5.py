import os
import sys
import math
import statistics
print("------ OS MODULE ------")
print("Current Directory:", os.getcwd())
print("Files in Directory:", os.listdir())
print("\n------ SYS MODULE ------")
print("Python Version:", sys.version)
print("Command Line Arguments:", sys.argv)
print("\n------ MATH MODULE ------")
num = 16
print("Square Root of 16:", math.sqrt(num))
print("2 raised to power 3:", math.pow(2, 3))
print("Value of Pi:", math.pi)
print("Factorial of 5:", math.factorial(5))
print("\n------ STATISTICS MODULE ------")
data = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard Deviation:", statistics.stdev(data))
1.that takes a list of product prices applies 18% GST to each price and dispaly the final price in py.
2.that calculates the total salary payout of all the employees in py.