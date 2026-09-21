num = int(input("Enter number:"))
number = str(num)
b = len(number)
for i in range(b):
    c = b-i-1
    ab = number[c]
    print(ab,end="")
