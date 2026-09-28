from functools import reduce as re
myList = [1,2,3,4,5]
print(myList)
print(re(lambda a,b: a + b ,myList))
