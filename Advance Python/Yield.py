def TestCase1():
    t1 = (x*x for x in range(1,11))
    print(t1)
    print()
    print(type(t1))
    
    
TestCase1()





def TestCase2():
    s = "Anvesh"
    yield s
    s1 = "Bunny"
    yield s1
    s2 = "Name1"
    yield s2
    

x = TestCase2()
print(next(x))
print(next(x))
print(next(x))
# print(next(x))




def TestCase2():
    s = "Anvesh"
    yield s
    s1 = "Bunny"
    yield s1
    s2 = "Name1"
    yield s2
    

x = TestCase2()
print(x)
for i in x:
    print(i)
    
    
y = TestCase2()
for i in y:
    print(i)
    
    
    
    
    
    
def SumofEle(L):
    s =0 
    for i in L:
        s+=i
    yield s 
    
x = SumofEle([1,2,3,4,5])
print(x)
print(next(x))





def odd(L):
    for i in L:
        if i%2==1:
            yield i 
            
x = odd([1,2,3,4,5])
print(x)
print(next(x))
print()
for i in x:
    print(i)
    
    
    
    
    
    
    
    
def nthlargest(L,n):
    maxele = []
    for i in range(n):
        m = 0
        for j in L:
            if j>m and j not in maxele:
                m = j
        maxele += [m] 
        yield m
        
L = [10,2,20,4,15]
n = int(input("Nth largest: "))
x = nthlargest(L,n) 
for i in range(n-1):
    next(x)

print(next(x))
    
        
        
        
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i 
            
x = factors(12)
print(next(x))
print(next(x))
print()
for i in x:
    print(i)
    
    
    
def isFactor(n,f):
    if n%f == 0:
        yield f
    else:
        yield f"{i} is not a factor of {n}"
        
n = int(input("Enter a number: "))



for i in range(1,n+1):
    print(next(isFactor(n,i)))