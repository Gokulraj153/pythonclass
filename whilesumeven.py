a = int(input("Enter the starting number:"))
b = int(input("Enter the ending number:"))
sum = 0
i = 1
while(i<=b):
   
    if a%2 ==0:
        print(sum + i)
        sum += a
        a += 1