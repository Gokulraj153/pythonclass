print("Type of Triangle")

A = int(input("Enter the value of A"))
B = int(input("Enter the value of B"))
C = int(input("Enter the value of C"))

if A==B and B==C:
    print("It is a equalateral triangle")
elif A==B or B==C:
    print("It is a isolateral triangle")
else:
    print("It is a Scalene Triangle")
