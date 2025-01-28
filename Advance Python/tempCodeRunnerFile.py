

class Example():
    def __init__(self,a,b,c):
        self.a = a
        self._b = b
        self.__c = c
        
    def getC(self):
        return self.__c
        

class Example2(Example):
    def M(self):
        print(self.a)
        print(self._b)

    

x = Example(10,20,30)
print(x.a)
print(x._b)
# print(x.__c)

print(x.getC())

x2 = Example2(1,2,3)
x2.M()