a = input("Enter the number:")#13234
for i in range(len(a)):
    ab =a[i]
    if (len(a))-1 == i:
        print(ab,end=".")
    else:
        print(ab,end=",")
    