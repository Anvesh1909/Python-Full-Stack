t1 = ()
print(t1)
print()
print(type(t1)) # <class 'tuple'>


t1 = (1001)
print(t1)
print()
print(type(t1)) # <class 'int'>


t1 = (1001,)
print(t1)
print()
print(type(t1)) # <class 'tuple'>

# for tuple () are optional. () by default 
t1 = 1001,
print(t1)
print()
print(type(t1)) # <class 'tuple'>

t1 = (1001,1002,1003,1004)
print(t1)
print()
print(type(t1)) # <class 'tuple'>

t1 = 1001,1002,1003,1004
print(t1)
print()
print(type(t1)) # <class 'tuple'>




# Insertion is preserved
#  to take input dynamically to tuple 
# 1,2,3,4,5,6
t1 = eval(input("enter the tuple data: "))
print(t1)
print()

for i in t1:
    print(i)


# duplicate objects are allowed
t1 = (1,2,3,4,2,3,1)
print(t1)
print()
print(type(t1)) 

# tuple is a immutable object(state_less object)
# t1[5] = 236468

print("min object is ", min(t1))
print("max object is ", max(t1))
print("len object is ", len(t1))

# Tuple is not dynamic or not growable
# t1.remove(1)



