word = "Python is an amazing language".split()
a,b,c,d,e = word
if len(a) > len(b) and len(c) and len(d) and len(e) :
    print(a)
elif len(b) > len(c) and len(d) and len(e) and len(a):
    print(b)
elif len(c) > len(b) and len(d) and len(e) and len(a):
    print(c)
elif len(d) > len(b) and len(c) and len(e) and len(a):
    print(d)
elif len(e) > len(c) and len(d) and len(b) and len(a):
    print(e)