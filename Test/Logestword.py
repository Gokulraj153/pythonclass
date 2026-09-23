word = "Python is an amazing language".split()
longest = word[0]
for i in word:
    if len(i) > len(longest):
        longest = i

print(longest)