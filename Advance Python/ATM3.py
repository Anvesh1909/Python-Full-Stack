# deposite, withdrawal, checkbalance, checkpin

# interface means only abstract methods 
# no implementation

# from abc import * 
from abc import ABC,abstractmethod

class BackInterface(ABC):
    @abstractmethod
    def deposite(self,amt): pass
    
    @abstractmethod
    def withdraw(self,amt): pass
    
    @abstractmethod
    def checkBalance(self): pass
    
    @abstractmethod
    def checkPin(self): pass


# back account
# Attributes
# account number, name, address, pin , amount 

# methods
# deposite, withdrawal, checkbalance, checkpin

class BankAccount(BackInterface):
    count = 0
    def __init__(self,name,address,pin):
        self.name = name
        self.address = address
        self.pin = pin
        self.accountNumber = BankAccount.count
        self.amount = 0
        BankAccount.count+=1
        
    def checkPin(self):
        '''
        input from user 
        check input and user pin
        return true if equal else false
        '''
        userInput = int(input("Enter pin: "))
        if self.pin == userInput:
            return True
        return False
        
    def checkBalance(self):
        '''
        check pin 
        if correct pin display balance else 
        display incorrect pin 
        '''
        if self.checkPin():
            print("Your balance is :",self.amount)
        else:
            print("Your pin is wronge please try again")

    def deposite(self):
        '''
        check pin 
        if correct 
            increase amount
        else 
            enter correct pin  
        '''
        amt = float(input("Enter amount: "))
        if self.checkPin():
            self.amount+= amt
            print("Deposited sucessfully")
        else:
            print("Your pin is wronge please try again")
    
    def withdraw(self):
        '''
        check pin 
        if correct 
            if amt > self.amoutn:
            decrease amount
        else 
            enter correct pin  
        '''
        amt = float(input("Enter amount: "))
        if self.checkPin():
            if amt>self.amount:
                print("insufficient balance")
            else:
                self.amount -= amt
                print("Amount withdraw successfully")
        else:
            print("Your pin is wronge please try again")
            
# A = BankAccount("Anvesh","Hyderabad",1234)
# A.deposite(100)
# A.withdraw(20)
# A.checkBalance()

# B = BankAccount("Bunny","Hyderabad",4321)
# B.deposite(1000)
# B.withdraw(500)
# B.checkBalance()
    
# accounts = []

# A = BankAccount("Anvesh","Hyderabad",1234)
# while True:
#     print('''
#           1. deposite 
#           2. withdral
#           3. checkBalance 
#           ''')
#     choice = int(input("Enter Your Choice : "))
#     if choice==1:
#         A.deposite(amt)
#     elif choice == 2:
#         A.withdraw(amt)
#     elif choice == 3:
#         A.checkBalance()
#     else:
#         print("enter Valid choice")



# A = BankAccount("Anvesh","Hyderabad",1234)
# dict {key account no : value account }


accounts = {}
while True:
    print("""
          1. create account
          2. select account
          3. exit
          """)
    choice = int(input("Enter your choice: "))
    if choice==1:
        name = input("Enter name: ")
        address = input("Enter address: ")
        pin = int(input("Enter pin: "))
        a = BankAccount(name,address,pin)
        accounts[a.accountNumber] = a
    elif choice == 2: 
        for k,v in accounts.items():
            print(k,": ",v.name)
        choice = int(input("Enter Account number: "))
        # a = accounts[choice]
        a = accounts.get(choice)
        
        if a:
            while True:
                print('''
                    1. deposite 
                    2. withdral
                    3. checkBalance 
                    4. exit
                    ''')
                choice = int(input("Enter Your Choice : "))
                if choice==1:
                    a.deposite()
                elif choice == 2:
                    a.withdraw()
                elif choice == 3:
                    a.checkBalance()
                elif choice == 4:
                    print("Thank you visit again")
                    break
                else:
                    print("enter Valid choice")
        else:
            print("Enter valid account number")
        
    elif choice == 3:
        
        break
    