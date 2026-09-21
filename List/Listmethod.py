myList = [10,20,30,40,50,20,70]
List_1 = [60,70,30,48,89]
#length
print(len(myList),"length")
#access
print(myList[3],"access")
print(myList[3:5],"access")
print(myList[:3],"access")
print(myList[1:],"access")
#List Method
#Adding Method - append()
myList.append(100)
print(myList,"append()")
#Adding Method - extend()
myList.extend(List_1)
print(myList,"extend")
#Adding Method - insert()
myList.insert(2,100)
print(myList)
#Removing Method - pop()
myList.pop()
print(myList,"pop")
print(myList.pop(6),"pop(6)")
#Removing Method - remove()
myList.remove(50)
print(myList)
#Removing Method - clear()
myList.clear()
print(myList)
myList = [10,20,30,40,50,20,70]
#Search & Count:
# index:
print(myList.index(40))
# count:
print(myList.count(70))

#Order & Copy:
#sort
myList.sort()
print(myList)
#reverse
myList.reverse()
print(myList)
#copy
my_list = myList.copy()
print(my_list)

for i in myList:
    if i <= 50:
        print(i,"loop")