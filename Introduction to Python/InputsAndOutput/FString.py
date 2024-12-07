name = "anvesh"
age = 12
sal = 892.92
l = [1,2,3,4]

print("string is %s"%name)
print("integer is %d"%age)
print("price is %f"%sal)
print("list is %s"%l)

print()
print("my name is %s my age is %d and my salary is %s list is %s"%(name,age,sal,l))

print("name is {} age {} sal {}".format(name,age,sal))
print("name is {1} age {0} sal {2}".format(age,name,sal))
print("name is {a} age {b} sal {c}".format(a = name,b = age,c = sal))
print(f"name is {name} age {age} sal {sal}")


