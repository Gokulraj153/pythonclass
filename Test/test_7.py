word = "Kamesh"
print(word)
word1 = list(word)
word1.remove("h")
word1.insert(0,"h")
for i in word1:
    print(i,end="")