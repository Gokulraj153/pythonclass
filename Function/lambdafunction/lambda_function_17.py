from functools import reduce
myList = [1,2,3,4,5,6]
print(myList)
even_numbers = filter(lambda a: a % 2 == 0, myList)
sum_evens = reduce(lambda a,b : a + b, even_numbers)
print(sum_evens)
