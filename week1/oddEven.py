def getNumber():
    return int(input("Enter a number: "))

def checkEvenOdd(num):
    return bool(num % 2 )

def pCheck(num):
    if checkEvenOdd(num):
        print(f"{num} - Odd")
    else:
        print(f"{num} - Even")

def main():
    n = getNumber()
    for _ in range(1,n+1):
        pCheck(_)

if __name__ == "__main__":
    main()