number = int(input("Enter the number"))
match(number):
    case n if n % 3 ==0 and n% 5 ==0:
        print("Number is divisible by both 3 and 5")
    case _:
        print("The number is not divisible by the both number")
