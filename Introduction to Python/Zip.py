l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

print(l1,l2)

t = tuple(zip(l1,l2))
print(t)






l1 = ["Pid", "Pname", "Price", "company"]
l2 = [1001,"mobile_1",23000.0, "Samsung"]


print()
print(l1,l2)

print()
d = dict(zip(l1,l2))
print(d)



l1 = ["Pid", "Pname", "Price", "company"]
l2 = [1001,"mobile_1",23000.0, "Samsung"]

for i,j in zip(l1,l2):
    print(i,":",j)

