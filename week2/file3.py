def main():
    units = int(input("Enter Units Consumed: "))
    bill = calcBill(units)
    print(f"Bill :{bill}")

def calcBill(u):
    if u <= 100:
        return u*1
    elif u <= 200:
        return 100 + 2*(u-100)
    else:
        return 300 + 3*(u-200)

if __name__ == "__main__":
    main()