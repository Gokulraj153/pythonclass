myList = [10,-10,20,-25,-35,65,34]
print(myList)
for i in range(len(myList)):
    if myList[i] <0:
        myList[i] = 0

print("The negative number are replaced by 0:",myList)