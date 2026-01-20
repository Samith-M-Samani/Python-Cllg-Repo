def main():
    input = [2,5,4,2,8,9,5,3,6,2,4]
    res = []
    c = 0
    for i in input:
        c += 1
        if input.count(i) > 1:
            input.pop(c)
        res.append(i)

    input.pop()

    print(input)

if __name__ == "__main__":
    main()