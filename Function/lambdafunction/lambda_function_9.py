myList = ["cat","elephant","dog","tiger"]
finalList = []
print(myList)
def longer(a):
    for i in a :
        if len(i) > 4 :
            finalList.append(i)

longer(myList)
print(finalList)