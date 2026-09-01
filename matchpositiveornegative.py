number = int(input("Enter the number"))

match(number):
    case number if number > 0:
        print("It is a positive number")
    case number if number < 0:
        print("It is a negative number")
    case number if number == 0:
        print("It is a Zero")
    case _:
        print("Number please")
