def search(list1,target):
    for i in list1:
        for j in list1:
            if(i + j == target):
                return i,j
    
    return -1,-1

def main():
    ls1 = [2,3,3,5,7,8,9]
    a,b = search(ls1,int(input("Enter Sum to Search: ")))
    if((a>-1 and b > -1) and a != b):
        print(f"{ls1.index(a)} and {ls1.index(b)}")
    else:
        print("not found")

if __name__ == "__main__":
    main()