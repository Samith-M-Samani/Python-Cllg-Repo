def week(i):
    switcher = {
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thursday",
        6:"Friday",
        7:"Saturday"
    }
    return switcher.get(i,"Invalid")

def main():
    print(week(int(input("Day No."))))

if __name__ == "__main__":
    main()