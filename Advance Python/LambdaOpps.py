
sal = [50,70,80,10]

# def increase(s):
#     return s+(20/100)*s

increase = lambda s: s+(20/100)*s

x = list(map(increase,sal))
print(x)




L = [13,11,14,5,6,9,19]

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

p = list(filter(prime,L))
print(p)




from functools import reduce
L = [1,2,3,4,5]

# def add(a,b):
#     return a+b

add = lambda a,b: a+b
x = reduce(add,L)
print(x)



class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        a = sum(self.marks)/len(self.marks)
        a = (a/10)*100
        return a

a = Students("A",[10,5,8,9,7])
b = Students("B",[8,6,7,4,6,1])

print(a.avg())
print(b.avg())








class Students:
    classStrenth = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Students.classStrenth += 1
    
    def avg(self):
        a = sum(self.marks)/len(self.marks)
        a = (a/10)*100
        return a

a = Students("A",[10,5,8,9,7])
b = Students("B",[8,6,7,4,6,1])
c = Students("B",[8,6,7,4,6,1])
d = Students("B",[8,6,7,4,6,1])
b = Students("B",[8,6,7,4,6,1])
b = Students("B",[8,6,7,4,6,1])


print(a.avg())
print(b.avg())

print(Students.classStrenth)
print(a.classStrenth)
print(c.classStrenth)







class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        a = sum(self.marks)/len(self.marks)
        a = (a/10)*100
        return a

    @staticmethod
    def syllabus():
        sub = ["m","p","c"]
        return sub
    

a = Students("A",[10,5,8,9,7])
b = Students("B",[8,6,7,4,6,1])

print(a.avg())
print(b.avg())


print(Students.syllabus())
print(a.syllabus())
print(b.syllabus())






class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        a = sum(self.marks)/len(self.marks)
        a = (a/10)*100
        return a

    @staticmethod
    def syllabus():
        return Students.sub
    
    @classmethod
    def setDetails(cls,name,sub,fee):
        cls.name = name
        cls.sub = sub
        cls.fee = fee
    
    @staticmethod
    def getDetails():
        print(Students.name)
        print(Students.sub)
        print(Students.fee)
    

a = Students("A",[10,5,8,9,7])
b = Students("B",[8,6,7,4,6,1])

Students.setDetails("Batch_38",["python","Apptitude","softskills"],25000)
Students.getDetails()
print(Students.syllabus())




from functools import reduce

class Arthmetic:
    
    value = 100
    
    def add(self,a,b):
        return a+b

    def mul(self,a,b):
        return a*b
    

class Statistics(Arthmetic):
    
    def __init__(self,marks):
        self.marks = marks
    
    def mean(self):
        s = reduce(self.add,self.marks)
        return s/len(self.marks)  
    
    
    
a = Statistics([10,20,30,40,50])
print(a.mean())  
print(a.value)







class Animal:
    def eat(self):
        print("Animal eats")

class Lion(Animal):
    def eat(self):
        # super().eat()
        print("Lion eats")
        
    def call(self):
        super().eat()
        self.eat()
l = Lion()
# l.eat()
l.call()






class Arthimatic:
    
    # def add(self,a,b):
    #     return a+b

    # def add(self,a,b,c):
    #     return a+b+c
    
    def add(self,*a):
        return sum(a)
    
    
a = Arthimatic()
print(a.add(2,4))
print(a.add(1,2,34))





# multiple inheritence
class A:
    # def M(self):
    #     print("A method")
    pass
        
class B:
    def M(self):
        print("B method")

class C:
    def M(self):
        print("C method")
        

class D(A,B,C):
    def M1(self):
        print("D method")
    pass
    

x = D()
x.M()
       
       
 
    
print(D.mro())





from abc import abstractmethod

# abstract class
class ATM:
    def display(self):
        print(self.amt)

    @abstractmethod
    def widthdraw(self,amt):
        pass
    
    @abstractmethod
    def deposite(self,amt):
        pass

class SBI(ATM):
    def __init__(self,amt):
        self.amt = amt
    
    def widthdraw(self,amt):
        self.amt -= amt
    
    def deposite(self,amt):
        self.amt += amt
        
s = SBI(100)
s.deposite(200)
s.widthdraw(50)
s.display()

        
        
        



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