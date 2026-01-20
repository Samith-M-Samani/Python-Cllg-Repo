def allag(listt):
    a = []
    b = []
    c = []
    for mark in listt: #int i = 0; i < arr.length; i++
        if mark > 80:   # if arr[i] >
            a.append(mark)
        elif mark > 50:
            b.append(mark)
        else:
            c.append(mark)
    return a,b,c

def main():
    marks = [23,65,85,29,78,93,46,62,39]

    A_grade = []
    B_grade = []
    C_grade = []
    A_grade,B_grade,C_grade = allag(marks)
    print(f"A grade Marks {A_grade}")
    print(f"B grade Marks {B_grade}")
    print(f"C grade Marks {C_grade}")

if __name__ == "__main__":
    main()