myList = [10,20,25,35,42]
counteven = 0
countodd = 0
for i in myList:
    if i % 2 == 0:
        counteven += 1
    else:
        countodd += 1

print("Total no of Even number in the list:",counteven)
print("Total no of Odd number in the list:",countodd)