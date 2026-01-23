

def linear(list1,ele):
    for i in list1:
        if(i == ele):
            return list1.index(i)
        
    return -1

def main():
    input1 = [1,3,5,6,7]
    print(linear(input1,int(input("Enter Num:"))))

if __name__ == "__main__":
    main()