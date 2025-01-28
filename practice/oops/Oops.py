# encapsulation 
# boading the code(atrributes and methods) in a single block
class Classname:
    # attributes
    # methods
    hello = 100
    def helloWorld(self):
        print("Hello world")
        
c = Classname()
print(c.hello)
c.helloWorld()





# inheritence 
# aquaring the properties(attributes and methods) of parent class to child class

class Parent:
    # attributes := height
    # methods := parentDetails
    height = 200
    def parentDetails(self):
        print("Class Parent with height 200")
        
class Child(Parent):
    # attributes := height and weight 
    # methods := parentDetails and childDetails
    weight = 200
    def childDetails(self):
        print("class Child with weight 200")
        
# type of inheritence 
# 1. single inheritence : one parent and one child
# 2. multi level inheritence  : one grandparent, one parent and one child
# 3. herachial inheritence  : single parent and multiple childs
# 4. multiple inheritence  : muliple parents and single child
# 5. hybrid inheritence  : more than one type of inheritence







# polymorphmism
# poly means many 
# morph means forms
# polymorphism means many forms


class Maths:
    # variable length argument
    def add(self,*argv):
        if len(argv)== 1:
            return argv[0]
        elif len(argv) == 2:
            return argv[0]+argv[1]
        else:
            s = 0
            for i in argv:
                s+=i
            return s
        
a = Maths()

# method overloading 
# same method name with diffrent number parameters
print(a.add(1))
print(a.add(1,2))
print(a.add(1,2,3))
print(a.add(1,2,3,4))




# method overiding
# same name with same number of parameter
# it cannot be done in same class two methods with same name and same number of parameters 
# it can be possible using inheritence 
class Parent:
    # methods : parent_constructor, parent_details, eat
    def __init__(self):
        print("Parent class constructor")
        
    def details(self):
        print("parent details")
        
    def eat(self):
        print("Parent eat")
        
class Child(Parent):
    # methods : parent_constructor, child_constructor, parent_details, child_details, eat
    def __init__(self):
        print("child class constructor")
        
    def details(self):
        print("child details")
    
    def parentCall(self):
        super().__init__()
        super().details()
        self.details()
        super().eat()
        self.eat()

# child class constructor overrides parent class constructor    
c = Child()  # child class constructor

# child class method overrides parent class method
c.details()  # child details
        
# how to call overided parent methods using super keyword
c.parentCall()
# Parent class constructor
# parent details
        




class Parent:
    def __init__(self):
        print("Parent class constructor")
        
    def details(self):
        print("parent details")
        
        
class Child(Parent):
    # methods := parent constructor, child_details, parent_details
    def details(self):
        print("child details")
        
        
c = Child()
c.details()
# Parent class constructor
# child details







# abstraction 
# hiding the internal implementation showing only functinalities
# that hides complex implementattion details while exposing only essential information and functionalities to the user 

# abstract method 
# created using @abstractmethod decorator
# @abstractmethod decorator should be imported from abc module

from abc import abstractmethod

# abstract class
class Collages:
    @abstractmethod
    def timeTable(self):
        pass

    @abstractmethod
    def exams(self):
        pass
    
    def uniform(self):
        print("without uniforms fine")
    
    
class DBATU(Collages):
    def timeTable(self):
        print("9:30 to 4:30")
        
    def exams(self):
        print("Exams will be start after pongal")

class MPGI(DBATU):
    def hostel(self):
        print("There are 10 hostels")

c = MPGI()
c.exams()
c.timeTable()
c.hostel()
c.uniform()




# interface 
# all abstract methods no normal methods

from abc import abstractmethod,ABC

# interface 
# contains only abstract methods 
class Collages(ABC):
    @abstractmethod
    def timeTable(self):
        pass

    @abstractmethod
    def exams(self):
        pass
    
     
    
class DBATU(Collages):
    def timeTable(self):
        print("9:30 to 4:30")
        
    def exams(self):
        print("Exams will be start after pongal")

class MPGI(DBATU):
    def hostel(self):
        print("There are 10 hostels")

c = MPGI()
c.exams()
c.timeTable()
c.hostel()
c.uniform()



# UPI 
# googlepay, phonepe, paytm 
# connets to bhimupi

# interface 
# bhimupi
# send, recive, checkbalence 

# google pay implements send
# phone pe implements send
# paytm implements send



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


