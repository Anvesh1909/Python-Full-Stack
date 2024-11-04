#upper case
ABC = 1001
print("ABC is :", ABC)
print()
print("Address is :", id(ABC))
print()
print("data type of ABC is :", type(ABC))
print()

#lower case
abc = 1001
print("abc is :", abc)
print()
print("Address is :", id(abc))
print()
print("data type of abc is :", type(abc))
print()


#combination of lower case , upper case and _
ABC_abc = 1001
print("ABC_abc is :", ABC_abc)
print()
print("Address is :", id(ABC_abc))
print()
print("data type of ABC_abc is :", type(ABC_abc))
print()

#combination of lower case , upper case , _ and number
ABC_abc_12345 = 1001
print("ABC_abc_12345 is :", ABC_abc_12345)
print()
print("Address is :", id(ABC_abc_12345))
print()
print("data type of ABC_abc_12345 is :", type(ABC_abc_12345))
print()


#only _ as a variable
_ = 1001
print("_ is :", _)
print()
print("Address is :", id(_))
print()
print("data type of _ is :", type(_))
print()

# many number _
_____ = 1001
print("_ is :", _)
print()
print("Address is :", id(_))
print()
print("data type of _ is :", type(_))
print()

# in python PVM will consider only 1 underscore( _ ) if we mention many _

# invalid identifiers
# _ _ , $ ,

# _ _ = 12
# $ = 123
# Abc_abc_$ = 233

print("case sensitive")

A = 1500 
a = 1200

print()
print("values of A and a :=", A, a)
print()
print("Addresses of A and a",id(A),id(a))



print("case insensitive")

A = 2024 
a = 2024

print()
print("values of A and a :=", A, a)
print()
print("Addresses of A and a",id(A),id(a))


import keyword as k

print(k.kwlist)
print("number of keywords: ", len(k.kwlist))

print(type(range(1,49)))
print(type([1,3,3]))
print(type(None))
