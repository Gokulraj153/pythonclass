n = int(input("Enter the value:"))
def positive(num):
    if num > 0:
        print("It is a Positive number")
    elif num < 0:
        print("It is a Negative number")
    elif num == 0:
        print("It is a Zero")

positive(n)