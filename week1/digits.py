def getNumber():
    return int(input("Enter Number: "))

def getDigits(n):
    d = 0
    while n > 0:
        n = n // 10
        d += 1
    return d
def main():
    num = getNumber()
    digits = getDigits()
    
    print(f"Number of digits: {digits}")
if __name__ == "__main__":
    main()