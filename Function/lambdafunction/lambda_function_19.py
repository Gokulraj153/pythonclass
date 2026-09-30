from functools import reduce
myList = [1,2,3,4,5,6]
print(myList)
odd_number = filter(lambda a: a % 2 != 0, myList)
square_odd = list(map(lambda a : a*a,odd_number))
add_square = reduce(lambda a,b : a + b, square_odd)
print(add_square)