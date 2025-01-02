# saperate functions for each functionality

class Students:
    def developers(self):
        print("Developers are responsible for writing the business logic")
    
    def angularDeveloper(self):
        print("Angular Developers are responsible for erp application development")
        
    def sqlDeveloper(self):
        print("SQL developers are responsible to perform database operations")


a = Students()
a.developers()
a.sqlDeveloper()
a.angularDeveloper()






class DuckTyping:
    def __init__(self,a):
        self.a = a
        
    def add(self,b):
        self.a += b
        return self.a
    
    def sub(self,b):
        self.a -= b
        return self.a
    
    def mul(self,b):
        self.a *= b
        return self.a
    
    def div(self,b):
        if b==0:
            return None
        self.a /= b
        return self.a
    
    def pow(self,b):
        self.a **= b
        return self.a
    
    def display(self):
        print(self.a)
    


a = DuckTyping(0)
a.add(10)
a.sub(1)
a.display()
a.mul(2)
a.div(10)
a.display()



 