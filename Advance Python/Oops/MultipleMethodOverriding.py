class Father1:
    def m1(self):
        print("Father1")
    pass

class Father2:
    # def m1(self):
    #     print("Father2")
    pass

class Child(Father1,Father2):
    # def m1(self):
    #     print("Child class")
    pass

# f1 = Father1()
# f1.m1()
# print()

# f2 = Father2()
# f2.m1()
# print()

c = Child()
c.m1()
