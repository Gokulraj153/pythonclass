print(" Grade Program ")
Grade = int(input("Enter your Marks"))

if 95 <= Grade <= 100: 
    print("Grade = S")
elif 80 <= Grade < 95:
    print("Grade = A")
elif 70 <= Grade < 80:
    print("Grade = B")
elif 60 <= Grade < 70:
    print("Grade = C")
elif 50 <= Grade < 60:
    print("Grade = D")
elif 35 <= Grade < 50:
    print("Grade = E")
else:
    print("Fail")
