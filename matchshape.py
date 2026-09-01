sides = int(input("Enter the number of sides: "))

match(sides):

    case 3:
        print("It is a Triangle")
    case 4:
        print("It is a Square or Rectangle")
    case 5:
        print("It is a Pentagon")
    case 6:
        print("It is a Hexagon")
    case 7:
        print("It is a Heptagon")
    case 8:
        print("It is a Octagon")
    case _:
        print("Enter the number under 10")
   
