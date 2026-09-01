num = int(input("Enter the number:"))

match(num):
    case n if 1<= n <=10:
        print("It is number in between 1 to 10")
    case _:
        print("It is not belong to the range")
