a = int(input("Enter the number:"))
if a > 1:

    for i in range(2,a):
        if a % i == 0:
            ab ="It is not a prime number"
        else:
            ab = "It is  a prime number"
else:
    ab = "It is not a prime number" 

print(ab)