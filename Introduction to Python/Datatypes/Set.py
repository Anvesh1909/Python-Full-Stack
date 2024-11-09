
s1 = {}
print(s1)
print()
print(type(s1))
print()

# to define a empty set
s2 = set()
print(s2)
print()
print(type(s2))
print()

s1 = set(input("enter the set data: "))

for i in s1:
    print(i)



# set is a mutable object (State full object):
s1 = {"A","B","C","D","E"}
print("before mutable operation")
print(s1)
print("after mutable operation")
# s1[1] = "z"


# set is a dynamic and growable:
s1 = set()

print("====initial set=====")
print(s1)

s1.add(1001)
s1.add("mobile")
s1.add(29000.50)

print("====after add opetaion====")
print(s1)

print("====after remove opetaion====")
s1.remove(1001)
print(s1)


# index and slice operaters is not applicable:
# print(s1[1]) 
print(s1[3:10])

