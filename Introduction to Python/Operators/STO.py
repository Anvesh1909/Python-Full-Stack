l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5] # address is diffrent
# l2 = l1 # address is same
# l2 = l1.copy() # address is diffrent


print(l1,l2)
print(id(l1),id(l2))
print(l1 is l2)
print(l1 is not l2)


# diffrence between == and is
l1 = [100,200,300,400]
l2 = [100,200,300,400]

print("list objects")
print(l1,l2)
print("Addresses")
print(id(l1), id(l2))
print("Using == operator ", l1 == l2)
print("Using is operator ",l1 is l2)




str1 = input("enter the string object : ")
str2 = "python supports membership operators it is a special type of operator (STO) in python. the main objective of membership operator is to search a charecter or group of character and return boolean values. following are the membership operators in python"
print(str1)

print(type(str1))

print()

print(str1 in str2)
