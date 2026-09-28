
myList = [10,20,30,40,50]
def printnum(num):
    sum = 0
    for i in num:
        if i%2 == 0:
            sum += i
    return sum

print(printnum(myList)) 