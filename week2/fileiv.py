ls1 = [2,4,3,2,3,5,6,6,6,6,2]
maxCount = ls1.count(ls1[0])
i = 0
num = ls1[0]
while i < len(ls1):
    if(ls1.count(ls1[i]) > maxCount):
        maxCount = ls1.count(ls1[i])
        num = ls1[i]
    i+=1
print(f"{maxCount} <== {num}")