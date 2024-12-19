class Students:
    def __init__(self):
        self.name = "anvesh"
        self.marks = 202

    def initialize(self):
        self.id = 2002
        self.z = "HEllo"
        print(self.marks)

    def delete(self):
        del self.marks
        del self.z


# declaring or defining or initializing

# inside the constructor
a = Students()
print(a.__dict__)

# inside the instance method
a.initialize()
print(a.__dict__)

# outside the class
a.presentDays = 23
print(a.__dict__)

print(a.marks)


# deleting an instance variable using del keyword using del keyword
a.delete()
print(a.__dict__)

del a.presentDays
print(a.__dict__)






class Operation_Class: 
    def __init__(self):
        self.a = 100
        self.b = 102
        print(self.a+self.b)


o = Operation_Class()
print(o)
print(id(o))
print(hex(id(o)))
