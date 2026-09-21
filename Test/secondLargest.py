myList = [10, 5, 20, 8, 20]
mySet = set(myList)
myList = list(mySet)
myList.sort()
print(myList[len(myList)-2])