class School:
    schoolName = "IHub"
    def __init__(self,name,rollno):
        # composition
        self.name = name
        self.rollno = rollno\
        # aggrigation
        print(School.schoolName)

x = School("Anvesh",1)
