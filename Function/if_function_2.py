n = int(input("Enter the value:"))
n1 = int(input("Enter the value:"))
n2 = int(input("Enter the value:"))
def positive(num,num2,num3):
    if num <= num2:
        print("n2 is Greater")
    elif num2 <= num3:
        print("n3 is Greater")
    else:
        print("n is Greater")

positive(n,n1,n2)