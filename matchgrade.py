mark = int(input("Enter the Mark: "))

match(mark):
    case n if 90< n <=100 :
        print("Grade = A")
    case n if 70< n <=90 :
        print("Grade = B")
    case n if 50< n <=70 :
        print("Grade = C")        
    case n if 35< n <=50 :
        print("Grade = D")
    case n if  n <35:
        print("Grade = Fail")
