a = int(input("Enter the starting number:"))
b = int(input("Enter the ending number:"))
c = 0
for i in range(a,b+1,7):
    print("7 x "+str(c + 1)+" = ",i)
    c +=1