myList = [1,3,2,5,6,4,0,7]
largest = myList[0]

for i in myList:
    if i > largest:
        largest = i

print(largest)