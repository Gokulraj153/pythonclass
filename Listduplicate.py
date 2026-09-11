myList=[10,20,10,30,50,60,20]
print(myList)
for i in myList:
    if myList.count(i) != 1:
        print(i,end=" ")

