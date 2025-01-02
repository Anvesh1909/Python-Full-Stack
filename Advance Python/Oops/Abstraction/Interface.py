from abc import *

class UPI(ABC):
    
    @abstractmethod
    def deposite(self,amt):
        pass
    
    @abstractmethod
    def withdraw(self,amt):
        pass
    
    @abstractmethod
    def balance(self):
        pass
    
class Phonepe(UPI):
    
    def deposite(self,amt):
        print("Amt deposite using phone pe")
    
    def withdraw(self,amt):
        print("Amt withdraw using phone pe")
    
    def balance(self):
        print("Amt balance using phone pe")


class Googlepay(UPI):
    
    def deposite(self,amt):
        print("Amt deposite using Googlepay ")
    
    def withdraw(self,amt):
        print("Amt withdraw using Googlepay")
    
    def balance(self):
        print("Amt balance using Googlepay")

name = input("Enter a name:")
u = globals()[name]
u.deposite(100)
u.withdraw(199)
u.display()
