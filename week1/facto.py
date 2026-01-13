def get_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * get_factorial(n - 1)
def getNumber():
    return int(input("Enter a number: "))

def main():
    num = getNumber()
    fact = get_factorial(num)
    print(f"Factorial of {num} is {fact}")

if __name__ == "__main__":
    main()