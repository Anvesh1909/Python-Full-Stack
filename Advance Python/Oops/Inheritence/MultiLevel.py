class A:
    def m1(self):
        print("A")
    
class B(A):
    def m2(self):
        print("B")

class C(B):
    def m3(self):
        print("C")

a = A()
a.m1()
print()

b = B()
b.m1()
b.m2()
print()

c = C()
c.m1()
c.m2()
c.m3()




class A:
    def m1(self):
        print("A")
    
class B(A):
    def m1(self):
        print("B")

class C(B):
    def m1(self):
        print("C")
        # A.m1()
        print(self)
        print(dir(self))
        super().m1()
        super(B,self).m1()
        
c = C()
c.m1()