l1 = [123,250,125,98]
# range in between 0, 256
res1 = bytes(l1)

print(type(res1))

print("encrypted : ",res1)

print("decripted : ",*res1)

# decript using for loop 

for i in res1:
    print(i)

# byte is immputable

# res1[0] = 12
# res2[1] = 134


# Byte array 
print("Byte array")

l1 = [1,2,3,4,5,6,7,8]

obj = bytearray(l1)

print(obj)
print(type(obj))

print("Encrypted : ", obj)
print("decrypt : ", *obj)

print("using for: ")
for i in obj:
    print(i)

# byte array is mutable object 
print("mutable object")

obj[0] = 101

print("Encrypted : ", obj)
print("decrypt : ", *obj)