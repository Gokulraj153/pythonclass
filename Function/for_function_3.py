n = int(input("Enter the value:"))
def printnum(num):
    for i in range(1,num+1):
        if i%3 == 0:
            print(i,end=" ")

printnum(n)