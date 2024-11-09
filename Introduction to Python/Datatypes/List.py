l1 = []

print(l1)
print()
print(type(l1))
print()

l2 = list()

print(l2)
print()
print(type(l2))
print()


l1 = [1002,19293,19392,12129,134321]

print(l1)
print()
print(type(l1))
print()

l1.append("Anvesh")
print(l1)

l1.remove(1002)
print("l1 =",l1)

# l1.remove("Anvfewfipe")
# Traceback (most recent call last):
#   File "c:\Users\manve\Desktop\Python-Full-Stack\Introduction to Python\List.py", line 27, in <module>
#     l1.remove("Anvfewfipe")
# ValueError: list.remove(x): x not in list


l2 = [1234,1233,1231,1322]

print("l2= ",l2)

l1.extend(l2)
# l1 += l2
# l1 = l1 + l2
print("after extends l1= ",l1)


print("L1 = ",l1)
l1 = l2.copy()
print("l2= ",l2)
print("after copy l1 =", l1)


l1.clear()
print(l1)


l1 = []

print("insert operation: ",l1)
l1.insert(0,100)
print("insert at 0 pos 100 : ",l1)
l1.insert(1,192)
print(l1)

l1.insert(-2,2838)
print(l1)


l1 = [1,2,3,4,5,6]

print(l1)

print("deleted element is ", l1.pop())

print(l1)

print("Pop index 3 that is",l1.pop(3))

print(l1)



l1 = [4,3,1,2]
print(l1)

# l2 = l1.sort() .sort() returns none so l2 is none 
l1.sort()

print("assending order :",l1)

l1.sort(reverse =  True)
print("reverse : ",l1)





a = "anvesh"
l = sorted(a)
print(l)
l = sorted(a,reverse=True)
print(l)





d = {1:3, 2:12, 3:433, 4:233}
print()
print(sorted(d))
print(sorted(d,reverse=True))




d = {1:3, 2:12, 3:433, 4:233}
print()
print(sorted(d.values()))
print(sorted(d.values(),reverse=True))



d = {1:3, 2:12, 3:433, 4:233}
print()
print(sorted(d.items()))
print(sorted(d.items(),reverse=True))