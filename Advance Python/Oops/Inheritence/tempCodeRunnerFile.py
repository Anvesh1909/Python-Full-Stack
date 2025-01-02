
class A:
    def __init__(self):
        print("A constructor")

    def aInstanceMethod(self):
        print("a instance method")
        
    @classmethod
    def aClassMethod(cls):
        print("a class method")

    @staticmethod
    def aStaticMethod():
        print("a static method")
        
        
class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")

    def aInstanceMethod(self):
        super().aInstanceMethod()
        print("B instance method")
        
    @classmethod
    def aClassMethod(cls):
        super().aClassMethod()
        print("B class method")

    @staticmethod
    def aStaticMethod():
        A.aStaticMethod()
        print("B static method")
        
        
b = B()
print("Calling b methods")
b.aInstanceMethod()
B.aClassMethod()
B.aStaticMethod()