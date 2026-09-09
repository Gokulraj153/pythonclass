maximum = int(input(" Please Enter the Maximum number : "))
total = 0
number = 1
while number <= maximum:
    if(number % 2 == 0):
        #print("{0}".format(number))
        total = total + number
    number = number + 1
print("The Sum of Even Numbers from 1 to N = ",total)