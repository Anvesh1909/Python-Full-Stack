
#  by default sting data type  taken by input

a = input("enter 1st value: ")
b = input("enter 2nd value: ")
print(a+b) # string value



a = int(input("enter 1st value: ")) # 45
b = int(input("enter 2nd value: ")) # 55
print(a+b) # 99


a = float(input("enter 1st value: ")) # 120.5
b = float(input("enter 2nd value: ")) # 120.5
print(a+b) # 141


a = complex(input("enter 1st value: ")) # 5 + 5j
b = complex(input("enter 2nd value: ")) # 2 + 2j
print(a+b) # 7 + 7j


a = bool(input("enter 1st value: ")) # 2923      |  1223   |
b = bool(input("enter 2nd value: ")) # dcjakebf  |         | 
print(a+b) # 2  |  1  |  0 


#  to read any type of data 
a = eval(input("enter anything : "))
print(a,"type of a is", type(a))

