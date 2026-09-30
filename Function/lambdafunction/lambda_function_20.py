from functools import reduce
myList = [1,2,3,4,5,6]
print(myList)
even_numbers = filter(lambda a: a % 2 == 0, myList)
square_even = list(map(lambda a : a*a*a,even_numbers))
sum_evens = reduce(lambda a,b : a + b, square_even)
print(sum_evens)
