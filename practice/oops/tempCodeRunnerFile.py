
class Students:
    strength = 0
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        Students.strength+=1
    
    def marks(self,marks):
        self.marks = marks
    
    def avg(self):
        print(Students.strength)
        print(Students.getStrength(1))
        print(Students.getClassStrength(1))
        return sum(self.marks)/len(self.marks)
    
    @staticmethod
    def getStrength(self):
        print(self.name)
        return Students.strength

    @classmethod
    def getClassStrength(cls):
        return cls.strength

a = Students("Anvesh",1)
a.marks([1,2,1,0,1,2])

p = Students("Prerna",2)
p.marks([9,8,9,8,9,8])

print(a.avg())
print(p.avg())
# instance variables or methods 


# static method or variables can be called inside instance method
# instance method or variable cannot be called inside the static or class methods