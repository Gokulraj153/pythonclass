
myList = [10,20,30,40,50]
def printnum(num):
    sum = 0
    for i in num:
        if i%2 == 0:
            sum += i
    print("Sum of even value:",sum)

printnum(myList) 