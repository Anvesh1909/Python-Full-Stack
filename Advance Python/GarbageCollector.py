import time

class Students:
    def __init__(self,name):
        self.name = name
        print("Student constructor")
        
    def __del__(self):
        time.sleep(2)
        print(self.name)
        print("Distructor for cleaning operations")


# usefull object
s1 = Students("Anvesh")
print(s1)

s2 = Students("Anvesh2")

# del s1,s2
# del s1
# print(s2.name)
# s1 = None


# useless object
# # del s1


# s2 = Students("Anvesh2")
# s1 = None
# s2 = None
# s1 = None
del s1

time.sleep(2)
print("End of an application")


# s2 = None
del s2