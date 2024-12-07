from EmployeeManagementSystem import Department,Hr,Login,Register

if __name__ == "__main__":
    Register.register("Anvesh",1,2,"Anvesh@gmail.com")
    print()
    Register.register("Anvesh",1,1,"Anvesh@gmail.com")
    print()
    Login.Login("Anvesh",1)
    print()
    Department.department(1,"Dept1","Bunny")
    print()
    Hr.hr(1,"ANvesh",23000,"22-09-2024")
    print()


