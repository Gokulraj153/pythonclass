numbers = [2,7,11,15]
target = 11 

found = False

seen = set()

for num in numbers:
    required = target - num
    if required in seen:
        found = True
        break

    seen.add(num)
print(found)