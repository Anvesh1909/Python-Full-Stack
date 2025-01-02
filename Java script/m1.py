class A:
    @classmethod
    def Cm(cls,name):
        cls.name = name
    
    def Im(self,name):
        self.name = name
        
        
a = A()
A.Cm("ANvesh")
a.Im("Nikhil")

print(A.name)
print(a.name)