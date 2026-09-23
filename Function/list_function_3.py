
myList = [50,32,60,12,3]
def printnum(num):
    smallest = num[0]
    for i in num:
        if smallest > i:
            smallest = i
    print("smallest value:",smallest)

printnum(myList) 