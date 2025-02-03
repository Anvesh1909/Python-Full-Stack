# 1
tuple1 = (10, 20, 30, 40, 50) 
print(tuple1[::-1])

# 2
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])



# 3
tuple1 = (50,)
print(tuple1)



# 4
tuple1 = (10, 20, 30, 40)
# a = tuple1[0]
# b = tuple1[1]
# c = tuple1[2]
# d = tuple1[3]
a,b,c,d = tuple1
print(f"tuple1 = ({a},{b},{c},{d})")



# 5
tuple1 = (11, 22)  
tuple2 = (99, 88)
tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)



# 6
tuple1 = (11, 22, 33, 44, 55, 66)
newTuple = tuple1[3:5]
print(newTuple)



# 7
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


# 8
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
key = []
value = []

for i in tuple1:
    key += [i[0]]
    value += [i[1]]
print(key)
print(value)

res = []
for i in range(1,len(value)+1):
    for j in range(0,len(value)-i):
        if value[j]>value[j+1]:
            key[j],key[j+1] = key[j+1],key[j]
            value[j],value[j+1] = value[j+1],value[j]
res = []
for i in range(len(value)):
    res += [(key[i],value[i])]
    
print(res)



tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
tuple1 = list(tuple1)

for i in range(1,len(tuple1)+1):
    for j in range(0,len(tuple1)-i):
        if tuple1[j][1]>tuple1[j+1][1]:
            tuple1[j],tuple1[j+1] = tuple1[j+1],tuple1[j]

print(tuple1)





# 9 
tuple1 = (50, 10, 60, 70, 50)
c = 0
for i in tuple1:
    if i==50:
        c+=1
print(c)





# 10
# tuple1 = (45, 45, 45, 45) 
tuple1 = (45, 45, 45, 5) 

res = False
for i in range(len(tuple1)-1):
    if tuple1[i] != tuple1[i+1]:
        print("False")
        break
else:
    print("True")
    
    
    
# 11
t1 = ()
t2 = tuple()
print(type(t1),type(t2))




# 12
t1 = ("Anvesh",True,22,25000.00,10+12j)
print(t1)




# 13
tuple1 = (50, 10, 60, 70, 50)
for i in tuple1:
    print(i)
    
    

# 14
t1 = (50, 10, 60, 70, 50)
t1 = list(t1)
t1.append(10)
t1 = tuple(t1)
print(t1)



# 15
tuple1 = (50, 10, 60, 70, 50)
print(tuple1[4])
print(tuple1[-4])



# 16
t1 = (50, 10, 60, 70, 50, 60)
res = []
for i in range(len(t1)):
    if t1[i] in t1[i+1:]:
        res+= [t1[i]]
print(res)



# 17
t1 = (50, 10, 60, 70, 50, 60)
ele = 11
for i in t1:
    if i == ele:
        print(True)
        break
else:
    print(False)





# 18
t1 = [50, 10, 60, 70, 50, 60]
t1 = tuple(t1)
print(t1)




# 19
t1 = (50, 10, 60, 70, 50, 60)
t1 = list(t1)
t1.remove(70)
t1 = tuple(t1)
print(t1)




# 20
t1 = (50, 10, 60, 70, 50, 60)
print(t1[1:4])




# 21
t1 = (50, 10, 60, 70, 50, 60)
ele = 70
i = 0
while i<len(t1):
    if t1[i] == ele:
        print(i)
        break
    i+=1
else:
    print("Ele not found")
    
    


# 22
t1 = (50, 10, 60, 70, 50, 60)
def length(L):
    c = 0
    for i in L:
        c+=1
    return c
print(length(t1))




# 23
t1 = (50, 10, 60, 70, 50, 60)
t2 = tuple(i for i in t1[::-1])
print(t2)




# 24
tuple1= (11, 22, 333, 44, 55)
a,b,c,d,e = tuple1
print(a)
print(b)
print(c)
print(d)
print(e)


# 25



# 26
t1 = (10,20,30,40,50) 
t1 = list(t1)
t1[2] = 33
t1 = tuple(t1)
print(t1)





# 27
tup1 = (18, 23, 2, 9) 
tup2 = (10, 3, 11) 

res = (tup1,tup2)
print("Tuple 1:",tup1)
print("Tuple 2:",tup2)
print("Tuples after Concatenating:",res)



# 28
aTuple = (100, 200, 300, 400, 500)  
aTuple[1] = 800  
print(aTuple) 


# 30
aTuple = (100, 200, 300, 400, 500)  
aTuple.pop(2)  
print(aTuple) 