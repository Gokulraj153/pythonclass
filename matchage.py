age = int(input("Enter your age: "))

match(age):

    case n if 1<= n <=12:
        print("It's a child")
    case n if 13<= n <=19:
        print("It's a Teen")
    case n if 20 <= n <= 59:
        print("It's a adult")
    case n if n >=60:
        print("It's a Senior")
    
