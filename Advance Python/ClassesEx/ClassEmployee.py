# - write a python script read the 4 employee information and display the 4 employee information by only creating 1 object


class Employees:

    def __init__(self,noOfEmployees):
        self.Emp = {}
        for i in range(1,noOfEmployees+1):
            name = input(f"Enter {i} name: ")
            sal = float(input(f"Enter {i} salary: "))
            self.Emp[i] = [name,sal]
            print()

    def display(self):
        for i in self.Emp.keys():
            print(f"info of employee {i} is: ")
            print(f"Employee name : {self.Emp[i][0]}")
            print(f"Employee salary : {self.Emp[i][1]}")
            print()



import time

Ihub = Employees(2)

time.sleep(3)

Ihub.display()

time.sleep(2)
print("End of an application")






