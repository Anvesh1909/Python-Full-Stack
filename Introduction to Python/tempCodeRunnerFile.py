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

t1.remove(1)