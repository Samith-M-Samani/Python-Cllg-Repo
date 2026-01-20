def main():
    result = []
    numbers = [3,5,2,4,1]
    add = 0
    for i in numbers:
        add += i
        result.append(add)

    print(result)

if __name__ == "__main__":
    main()