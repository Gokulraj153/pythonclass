a = [10,20,30,40,50,10,20]
b = [10,40,30,60,70,80,10,20]
x = set(a)
y = set(b)
common = x.intersection(y)
common1 = list(common)
print(common1)
for i in range(len(common1)):
    print(i,"iteration")
    print(a.count(a[i]))
    #if common1[i] == (a.count[a[i]] and b.count[b[i]] > 1):
    #    print(set(common1[i]))
