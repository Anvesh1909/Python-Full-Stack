class Students:
    strength = 45

    def __init__(self):
        Students.location = "Hyderabad"

    def instanceMethod(self):
        Students.est = 2024
        print("inside instance method",Students.strength)
        # cannot possible
        # del Students.z
        # print("Del z outside class")
        
    @classmethod
    def classMethod(cls):
        cls.name = "ihub"
        print("inside class method",Students.strength)
        
    @staticmethod
    def staticMethod():
        Students.z = 1010
        print("inside static method",Students.strength)
        Students.strength = 24
        print("inside static method After updating",Students.strength)
        del Students.z
        print("Del z inside static method")
        Students.z = 0    


a = Students()

print("outside the class",Students.strength)

a.instanceMethod()

Students.classMethod()

Students.staticMethod()

# print(a.__dict__)

# print(Students.__dict__)


print(Students.est)
print("Z=",Students.z)


Students.z = 102020
print("Z=",Students.z)

del Students.z
print("Del z outside class")