from functools import reduce
myList = ["Python","is","awesome"]
print(reduce(lambda a,b: a+" "+b,myList))
