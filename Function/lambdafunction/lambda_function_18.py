myList = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda a: a % 2 == 0, myList))

print(len(even_numbers))
