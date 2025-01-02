from abc import *

class Students:
    
    @abstractmethod
    def addStudents(self):
        pass
    

s1 = Students()
s1.addStudents()