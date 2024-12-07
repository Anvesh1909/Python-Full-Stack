l = []

for i in range(1,100):
    if i %2 == 0:
        l.append(i)

print(l)


l = [ i for i in range(1,100) if i%2 == 0]

print(l)



d = { k: k*k  for k in range(1,11) }

print(d)



t = (i for i in range(1,21) if i%2 == 0)


# print(*t)

for i in t:
    print(i)



l = [1,2,3,4,5,6,76,34,122]


mul = [ i for i in l if i%3== 0]

print(mul)



name = ["ANvesh","surya","Deepak"]
roll = [1,2,3]


d = { roll[i] :name[i]  for i in range(len(name)) }

print(d)



l = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]


l = [ j for i in l for j in i]

print(l)