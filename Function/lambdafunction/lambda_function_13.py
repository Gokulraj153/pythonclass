from functools import reduce as re
myList = [4,10,7,25,3]
print(myList)
print(re(lambda a,b: a if a > b else b ,myList))
