class Students:

    # default construstor 
    def __init__(self):
        print("Student constructor method")


Anvesh = Students()  # object reference variable

Bunny = Students()  # another object 



class Students:
    def __init__(self):
        self.roll = 101
        self.name = "Anvesh"
        self.age = 22
    
    def display(self):
        print(self.roll,self.name,self.age)


Anvesh = Students()
Anvesh.display()






class Students:
    def __init__(self,roll,name,age):
        self.roll = roll
        self.name = name
        self.age = age
    
    def display(self):
        print(self.roll,self.name,self.age)


Anvesh = Students(191,"ANvesh",21)
Anvesh.display()


Bunny = Students(193,"Bunny",22)
Bunny.display()



