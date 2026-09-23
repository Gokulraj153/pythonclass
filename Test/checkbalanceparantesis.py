symbol = input("Enter parentheses:")

count = 0
balanced = True

for ch in symbol:

    if ch == "(":
        count += 1

    elif ch == ")":
        count -= 1

        if count < 0:
            balanced = False
            break

if count != 0:
    balanced = False
print(balanced)