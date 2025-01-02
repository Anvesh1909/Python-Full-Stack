class Students:
    name = 1
    _marks = []
    __fee = 0
    
    def __init__(self,name,marks,fee):
        self.StudentId = name
        self._marks = marks
        self.__fee = fee
        
    def getDetails(self):
        print(self.StudentId)
        print(self._marks)
        print(self.__fee)
        
Students