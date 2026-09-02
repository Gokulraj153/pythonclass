a = int(input("Enter the starting number:"))
b = int(input("Enter the ending number:"))
sum = 0
for i in range(a,b+1):
    if i%2 !=0:
        print(sum + i)
        sum += i