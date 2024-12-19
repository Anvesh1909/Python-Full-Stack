class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        
class Students(Person):
    def __init__(self,name,age,sid):
        super().__init__(name,age)
        self.sid = sid
        
    def display(self):
        super().display()
        print("Student id : ",self.sid)
        
        

a = Person("Anvesh",22)
a.display()

print()

a = Students("Anvesh",22,1)
a.display()





class Register:
    strength = 0
    def __init__(self,name,id,fee):
        self.name = name
        self.id = id
        self.fee = fee
        Register.strength +=1
        
class Students(Register):
    def __init__(self,name,id,fee,marks):
        super().__init__(name,id,fee)
        self.marks = marks
    
    def display(self):
        print(self.name,self.id,self.fee)
        print(self.marks)
        print("Class Strength =",super().strength)
        

a = Students("Anvesh",1,500000,75)
a = Students("Anvesh",1,500000,75)
a = Students("Anvesh",1,500000,75)
a = Students("Anvesh",1,500000,75)
a.display()






class ReserveBank:
    
    networthAmt = 0
    def __init__(self,name,networth):
        self.name = name
        ReserveBank.networthAmt = 0
        
        
    @staticmethod
    def networth():
        print(ReserveBank.networthAmt)
    @staticmethod
    def addAmt(amt):
        ReserveBank.networthAmt+=amt
        
        
    
class Sbi(ReserveBank):
    bankAmt = 0
    def __init__(self,name):
        super().__init__(name,0)
        self.accountMoney = 0
        
    
    def deposite(self,amt):
        # ReserveBank.networthAmt+=amt
        super().addAmt(amt)
        self.accountMoney += amt
        Sbi.bankAmt
        
        
        
class Canara(ReserveBank):
    bankAmt = 0
    def __init__(self,name):
        super().__init__(name,0)
        self.accountMoney = 0
        
    
    def deposite(self,amt):
        # ReserveBank.networthAmt+=amt
        super().addAmt(amt)
        self.accountMoney += amt
        Canara.bankAmt += amt


    
   

a = Canara("Anvesh")
b = Sbi("Surya")

a.deposite(100)
b.deposite(200)

a.networth()








class A:
    def __init__(self):
        print("A Constructor")
        
class B(A):
    
    # def __init__(self):
    #     super().__init__()
    #     print("B constructor")
    
    def m1(self):
        super().__init__()
        super().__init__()

    
b = B()
b.m1()





class A:
    def __init__(self):
        print("A constructor")

    def aInstanceMethod(self):
        print("a instance method")
        
    @classmethod
    def aClassMethod(cls):
        print("a class method")

    @staticmethod
    def aStaticMethod():
        print("a static method")
        
        
class B(A):
    def __init__(self):
        print("B constructor")

    def bInstanceMethod(self):
        print("B instance method")
        
    @classmethod
    def bClassMethod(cls):
        print("B class method")

    @staticmethod
    def bStaticMethod():
        print("B static method")
        
        
b = B()
print("Calling b methods")
b.bInstanceMethod()
B.bClassMethod()
B.bStaticMethod()
        

print("From b instance calling a")
b.aInstanceMethod()
B.aClassMethod()
B.aStaticMethod()













class A:
    def __init__(self):
        print("A constructor")

    def aInstanceMethod(self):
        print("a instance method")
        
    @classmethod
    def aClassMethod(cls):
        print("a class method")

    @staticmethod
    def aStaticMethod():
        print("a static method")
        
        
class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")

    def aInstanceMethod(self):
        super().aInstanceMethod()
        print("B instance method")
        
    @classmethod
    def aClassMethod(cls):
        super().aClassMethod()
        print("B class method")

    @staticmethod 
    def aStaticMethod():
        A.aStaticMethod()
        print("B static method")
        
        
b = B()
print("Calling b methods")
b.aInstanceMethod()
B.aClassMethod()
B.aStaticMethod()
        

