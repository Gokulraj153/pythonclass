word = "hello"
print(word)
word1 = list(word)
word1.remove("o")
word1.insert(0,"o")
for i in word1:
    print(i,end="")