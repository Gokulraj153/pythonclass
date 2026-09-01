n1 = int(input("Enter the num1:"))
op = input("Enter the operation:")
n2 = int(input("Enter the num2:"))

match(op):

    case op if op == "+":
        print(n1+n2)
    case op if op == "-":
        print(n1-n2)
    case op if op == "*":
        print(n1*n2)
    case op if op == "/":
        print(n1/n2)
    case _:
        print("operation please")
