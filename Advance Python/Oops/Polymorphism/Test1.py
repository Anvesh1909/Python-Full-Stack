class A:
    def __init__(self):
        print("Hello")
        
        
a = A()

print(a)

print(hex(id(a)))


class A:
    def __init__(self,item):
        self.item = item
        
    def __str__(self):
        return str(self.item)
    

a = A(100)
print(a)

b = A(200)
print(b)

# print(a+b)




class A:
    def __init__(self,item):
        self.item = item
        
    def __str__(self):
        return str(self.item)
    
    def __add__(self,other):
        return self.item + other.item
    
    def __sub__(self,other):
        return self.item - other.item
    
    def __mul__(self,other):
        return self.item * other.item
    
    def __truediv__(self,other):
        return self.item / other.item
    
    def __floordiv__(self,other):
        return self.item // other.item
    
    def __pow__(self,other):
        return self.item - other.item
    
    def __mod__(self,other):
        return self.item % other.item
    

a = A(100)
print(a)

b = A(200)
print(b)

print(a+b)
print(a*b)
print(a/b)




class A:
    def __init__(self,item):
        self.item = item
        
    def __str__(self):
        return str(self.item)
        
    def __add__(self,other):
        obj = A(self.item + other.item)
        return obj
    
    
a = A(10)
b = A(5)
c = A(20)

print(a+b+c)  


class A:
    def __init__(self,item):
        self.item = item
        
    def __str__(self):
        return str(self.item)
        
    def __imul__(self,other): 
        obj = A(self.item * other.item)
        return obj
    
    def __iadd__(self,other):
        obj = A(self.item + other.item)
        return obj
    
a = A(10)
b = A(20)
c = A(30)

a+=b
print(a)
a*=b
print(a)
    






class Math1:
    def __init__(self,operand):
        self.operand1 = operand
        
    def __str__(self):
        return str(self.operand1)
    
    def __add__(self,operand2):
        obj = Math1(self.operand1+operand2)
        return obj
    
    def __iadd__(self,operand2):
        obj = Math1(self.operand1+operand2)
        return obj
    
    def __mul__(self,operand2):
        obj = Math1(self.operand1*operand2)
        return obj
    
    def __imul__(self,operand2):
        obj = Math1(self.operand1*operand2)
        return obj
    

a = Math1(10)
a = a+20     
print(a)

a = a*10
print(a)

a+=10
print(a)

a *= 10
print(a)

print()







class Palindrome:
    def __init__(self,w):
        self.w = w
    
    def __str__(self):
        i = 0 
        j = len(self.w)-1
        while i<j:
            if self.w[i] != self.w[j]:
                return str(False)
            i+=1
            j-=1
        return str(True)
    
    
a = input("Enter name: ")
print(Palindrome(a))
    
