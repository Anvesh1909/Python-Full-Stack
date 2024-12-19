class Father1:
    def m1(self):
        print("Father1")

class Father2:
    def m2(self):
        print("Father2")

class Child(Father1,Father2):
    def m3(self):
        print("Child class")

f1 = Father1()
f1.m1()
print()

f2 = Father2()
f2.m2()
print()

c = Child()
c.m1()
c.m2()
c.m3()