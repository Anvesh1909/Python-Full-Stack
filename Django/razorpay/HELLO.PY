class Student:
    def __init__(self):
        self.name = "ANvesh"
        self.rollno = '21'

    def __str__(self):
        return f"my name is {self.name}, my roll no is {self.rollno}"

    
    

s1 = Student()
print(type(s1))
print(s1)


# details = s1.__str__()
details = str(s1)
print(type(details))
print(details)
