from abc import * 
class Students(ABC):
    @abstractmethod
    def m1(self):
        pass
    
    # @abstractmethod
    def m2(self):
        print("M2")
    
class IhubStudents(Students):
    def m1(self):
        print("IhubStudents m1")
    
    
# s1 = IhubStudents()
# TypeError: Can't instantiate abstract class IhubStudents without an implementation for abstract method 'm2'

# concrete class
class Ihub(IhubStudents):
    # def m2(self):
    #     print("Ihub M2")
    pass
        
s1 = Ihub()
s1.m1()
s1.m2()