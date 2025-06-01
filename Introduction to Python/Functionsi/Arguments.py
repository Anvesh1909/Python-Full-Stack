# positional arguments:

def positional(a,b,c):
    print(a,b,c)

positional(1,2,3) # positional arguments same as formal order



# default arguments
def default(a,b=10):  # default parameter
    print(a*b)

default(5) # b is 10 by default
default(10,20) # b is updated with 20






def division(a,b=1):
    return a/b

def details(name,age,gender=None,address=None):
    print("name",name)
    print("age",age)
    print("gender",gender)
    print("Address",address)

def phoneNo(ph1,ph2=None):
    print(ph1)
    if ph2:
        print(ph2)

phoneNo(123)
phoneNo(122,1234)





# keyword arguments

def keyboard(a,b,c):
    print(a,b,c)

keyboard(b=10,a=20,c=30)


# - write a python script display the employee details using default and keyword arguments

def employee(name,age,phone,alternateno=None):
    print(name)
    print(age)
    print(phone)
    if alternateno:
        print(alternateno)


employee(phone=8019342575,age=22,name="anvesh")





# variable length arguments
def add(*x):
    sum = 0
    for i in x:
        sum+=i
    return sum

print(add(1,2,3,4,5))





# keyword variable length arguments
def KVLargumant(**kargv):
    for k,v in kargv.items():
        print(k,":",v)

KVLargumant(name="Anvesh",phone=80182,sal=2333.93993)

