myList = [11,34,23,54,68,46,0,87]
largest = myList[0]
Largenum =[]
print(myList,"Original List")
for i in myList:
    if i > largest:
        largest = i
        Largenum.append(largest)
length = len(Largenum)
print(Largenum,"Largest number")
print(Largenum[length-2], "Second Largest number")