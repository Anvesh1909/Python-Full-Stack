

class Example():
    def __init__(self,a,b,c):
        self.a = a
        self._b = b
        self.__c = c
        
    def getC(self):
        return self.__c
        

