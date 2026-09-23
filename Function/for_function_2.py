n = int(input("Enter the value:"))
def printnum(num):
    sum = 0
    for i in range(1,num+1):
        if i%2 == 0:
            sum += i
    print("Sum of even value:",sum)

printnum(n)