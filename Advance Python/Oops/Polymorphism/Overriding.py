class Register:
    register = {}
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation
        Register.register[self.name] = self.occupation  
        
    def M(self):
        print("Name: ",self.name)
        print("Occupation: ",self.occupation)
       
    @staticmethod 
    def display():
        print(Register.register)
        
        
class Student(Register):
    def __init__(self,name,rollno):
        super().__init__(name,"Student")
        self.rollno = rollno
    
    def M(self): 
        super().M()
        print("Rollno: ",self.rollno)
    

class Teacher(Register):   
    def __init__(self,name,occupation,eno):
        super().__init__(name,"Teacher")
        self.eno = eno

    def M(self):
        super().M()
        print("Eno: ",self.eno) 
        
        
a = Student("Anvesh",101)
b = Teacher("Surya",102,1001)

a.M()
b.M()
Register.display()

    