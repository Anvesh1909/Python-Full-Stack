class A:
    def M(self):
        print("M zreo argument")
        
    def M(self,a):
        print("M one arguments")
        
    def M(self,a,b):
        print("M two arguments")
        
obj = A()
# obj.M()
# obj.M(1)
# obj.M(1,2)

# obj.M()
# obj.M(1)
obj.M(1,2)



# method overloading with default argument:
class A:
    def M(self,a=None,b=None,c=None):
        if a==None and b==None and c==None:
            print("M zreo argument")
        elif a!=None and b==None and c==None:
            print("M one argument")
        elif a!=None and b!=None and c==None:
            print("M two argument")
        elif a!=None and b!=None and c!=None:
            print("M three argument")
            
            
a = A()
a.M()
a.M(1)
a.M(1,2)
a.M(1,2,3)




## method overloading using variable lenght argument:
class A:
    def M(self,*argv):
        print(len(argv),"length argument")
        
a = A()
a.M()
a.M(1)
a.M(1,2)
a.M(1,2,3)
a.M(1,2,3,4)



## constructor overloading
class A:
    def __init__(self):
        print("__init__ zreo argument")
        
    def __init__(self,a):
        print("__init__ one arguments")
        
    def __init__(self,a,b):
        print("__init__ two arguments")
        
        
# a = A()
# a = A(1)
# a = A(1,2)

# a = A()
# a = A(1)
a = A(1,2)



# constuctor overloading with default argument:

class A:
    def __init__(self,a=None,b=None,c=None):
        if a==None and b==None and c==None:
            print("__init__ zreo argument")
        elif a!=None and b==None and c==None:
            print("__init__ one argument")
        elif a!=None and b!=None and c==None:
            print("__init__ two argument")
        elif a!=None and b!=None and c!=None:
            print("__init__ three argument")
            
            
a = A()
a = A(1)
a = A(1,2)
a = A(1,2,3)




## constructor overloading using variable lenght argument:
class A:
    def __init__(self,*argv):
        print(len(argv),"length argument")
        
a = A()
a = A(1)
a = A(1,2)
a = A(1,2,3)




