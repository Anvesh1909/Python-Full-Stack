try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    print(a/b)
except ArithmeticError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("Error by default except")
finally:
    print("Finally block")
    
    

import os

try:
    os._exit(1)
    print(10/0)
except ArithmeticError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("Error by default except")
finally:
    print("Finally block end of application")
    
    
import os

try:
    print("Start application")
    os._exit(True)
    print(10/0)
except ArithmeticError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("Error by default except")
finally:
    print("Finally block end of application")
    
    
    
   
import os

try:
    print("Start application")
    os._exit(True)
    print(10/0)
except ArithmeticError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("Error by default except")
finally:
    print("Finally block end of application")
    
    
    
def abcd(a):
    pass
abcd()


try:
    def abcd(a):
        pass
    abcd()  
except TypeError as e:
    print(e)
    
import os
os._exit(10)

import os
os._exit("A")



try:
    print("try")
    a = 10//0
except:
    print("Except")
    a = 10//0
finally:
    print("Finally")
    
    
    

try:
    print("Java Developer")
except:
    print("Angular developer")
else:
    print("react developer")
finally:
    print("Finally block")




try:
    print("inner try block")
    try:
        print("inner try block")
    except:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
    
    
    
    

try:
    print("inner try block")
    20//0
    try:
        print("inner try block")
    except:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
    
    




try:
    print("inner try block")
    try:
        1000/0
        print("inner try block")
    except:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
    






try:
    a=10
except:
    print("Except")
print(a)

if a==10:
    b = 20
print(b)

if a == 1:
    c = 20
print(c)






try:
    a = eval(input("Enter number: "))
    print(a)
except ArithmeticError as e:
    print(e)
except:
    print("Except block")
else:
    print("result :",a)
finally:
    print("finally")