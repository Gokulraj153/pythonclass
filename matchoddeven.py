n1 = int(input("Enter the number:"))

match (n1%2==0):

    case True:
        print("It is a even number")
    case False:
        print("It is a odd number")
    case _:
        print("It is not a number")
