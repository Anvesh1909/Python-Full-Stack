class ATM:
    def __init__(self):
        self.name = input("Enter name :")
        self.pin = int(input("Enter pin: "))
        self.bal = float(input("Enter initial balance: "))

    def checkPin(self):
        p = int(input("Enter pin: "))
        if p == self.pin:
            return True
        return False
     
    def balance(self):
        if self.checkPin():
            print("Your balance is : ",self.bal)
        else:
            print("invalid pin")

    def withdraw(self):
        amt = float(input("Enter amount to withdraw : "))
        if self.checkPin():
            if amt < self.bal:
                self.bal -= amt
                print(amt,"amount withdraw")
            else:
                print("Your balance is insufficient")
        else:
            print("invalid pin")
    
    def deposite(self):
        if self.checkPin():
            amt = float(input("Enter the amount to deposite: "))
            self.bal += amt
            print(amt,"successfully credited to your account")
        else:
            print("invalid pin")


account = {}

while True:
    print("""
    1. Create account
    2. Select account
    """)
    option = int(input("Enter your choise : "))

    if option == 1:
        a = ATM()
        account[a.name] = a

    elif option == 2:
        for i in account.keys():
            print(i)
        name = input("Enter your name : ")
        a = account.get(name)

        if a != None:
            while True:
                print('''
                    1. balance enquary 
                    2. withdraw 
                    3. deposite
                    4. exit
                ''')
                option = int(input("Enter you choice: "))

                if option == 1:
                    a.balance()
                elif option == 2:
                    a.withdraw()
                elif option == 3:
                    a.deposite()
                elif option == 4:
                    print("")
                    break
        else:
            print("Enter valid name")

