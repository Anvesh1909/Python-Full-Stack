sq = lambda a : a*a

print(sq(5))
print(sq(5.5))

add = lambda a,b: a+b

print(add(10,20))


display = lambda a : print([i for i in range(a)])
display(10)



# filter
L = [1,2,3,4,5,6,7,8,9]
l = list(filter(lambda x : x%2==0,L))
print(L)
print(l)


# map

l1 = [1,2,3,4,5]
l2 = list(map(lambda x:x*100 ,l1))
print(l1)
print(l2)