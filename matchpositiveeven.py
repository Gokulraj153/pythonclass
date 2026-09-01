number = int(input("Enter the number"))#0

match(number):
    case n if n %2==0 and n > 0:
        print("It is a Positive even")
    case n if n %2!=0 and n > 0:
        print("It is a Positive odd")
    case n if n < 0:
        print("It is a Negative number")
    case n if n == 0:
        print("It is equal to zero")
