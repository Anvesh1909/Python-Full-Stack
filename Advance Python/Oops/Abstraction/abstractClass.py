from abc import *

class Students(ABC):
    pass

s1 = Students()



from abc import * 

class Student(ABC):
    @abstractmethod
    def addStudents(self):
        pass
    
class AddStudents(Student):
    def addStudents(self):
        print("add Students")
        
s1 = AddStudents()
s1.addStudents()