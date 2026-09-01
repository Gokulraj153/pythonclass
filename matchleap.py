year  = int(input("Enter the year: "))

match(year):
    case n if n % 400 ==0 or n %4 ==0  :
        print("It is a Leap year")
    case _:
        print("It is not a Leap year")
