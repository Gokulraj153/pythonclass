myList = [1,2,3,4,5,6]
even_numbers = filter(lambda a: a % 2 == 0, myList)
squared_evens = list(map(lambda a: a * a, even_numbers))
print(squared_evens)
