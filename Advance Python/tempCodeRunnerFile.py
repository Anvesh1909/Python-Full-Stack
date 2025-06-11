
def TestCase2():
    s = "Anvesh"
    yield s
    s1 = "Bunny"
    yield s1
    s2 = "Name1"
    yield s2
    

x = TestCase2()
print(next(x))
print(next(x))
print(next(x))