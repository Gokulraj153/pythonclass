myList = [1,3,2,5,6,4,0,7]
smallest = myList[0]

for i in myList:
    if i < smallest:
        smallest = i

print(smallest,"Smallest")