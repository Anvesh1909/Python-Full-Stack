class Parent:
    def m1(self):
        print("Parent Class")
class Child1(Parent):
    def m2(self):
        print("Child1 class")
class Child2(Parent):
    def m3(self):
        print("Child2 class")


p = Parent()
p.m1()
print()

c1 = Child1()
c1.m1()
c1.m2()
print()


c2 = Child2()
c2.m1()
c2.m3()
print()