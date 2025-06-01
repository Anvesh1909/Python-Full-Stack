# 1. print Hello world
print("Hello world!")

# 2. sep attribute 
print(1,2,3,4,sep=",")

# 3. end attribute
print("anvesh",end="")
print()

# 4. add 2 numbers
a = 10
b = 20
print(a+b)

# 5. return a sum of list
l = list(1,2,3,4,5)
l = [1,2,3,4,5]
print(sum(l))

# 6. return largest element in list
l = [1,2,3,4,5]
print(max(l))

# 7. return minimum element in list
l = [1,2,3,4,5]
print(min(l))

# 8. add element in list at end
l = [1,2,3,4,5]
l.append(6)

# 9. remove element at last
l = [1,2,3,4,5]
l.pop()

# 10. remove element at index
l = [1,2,3,4,5]
l.pop(1)

# 11. insert at position
l = [1,2,3,4,5]
l.insert(1,10)

# 12. remove all elements in list 
l = [1,2,3,4,5]
l.clear()

# 13. slicing in tuple
t = tuple(1,2,3,4,5)
t = (1,2,3,4,5)
print(t[1:])

# 14. to reverse a tuple 
t = (1,2,3,4,5)
print(t[::-1])

# 15. to display tuple by 2 steps 
t = (1,2,3,4,5)
print(t[::2])

# 16. to reverse and start form -2
print(t[-2::-1])

# 17 declare a set
s = set(1,2,3,4,5)
s = {1,2,3,4,5}
print(s)

# 18 add an element to set
s = {1,2,3,4,5}
s.add(12)
print(s)

# 19 remove an element in set
s = {1,2,3,4,5}
s.remove(1)
print(s)

# 20 declare a dict
# d = dict(2=4,1=9)
d = {2:4,3:9,4:16,5:25}
print(d)

# 21 add element in dict
d = {2:4,3:9,4:16,5:25}
d[6] = 36
print(d)

# 22 get element in dict
d = {2:4,3:9,4:16,5:25}
print(d.get(5))

# 23 get element id not return -1
d = {2:4,3:9,4:16,5:25}
print(d)
print(d.get(8,-1))

# 24 assignment operator
a = 10
b = 10
a+=b
print(a)

# 25 assignment operator
a = 10
b = 20

a*=b
print(a)

# 26 assignment operator
a = 10
b = 2

a**=b
print(a)

# 27 assignment operator
a = 10
b = 20

a/=b
print(a)

# 28 assignment operator
a = 10
b = 20

a//=b
print(a)

# 29 Equality operator
a = 10
b = 20 

print(a==b)
print(a!=b)

# 30 relational operator
a = 20
b = 20

print(a>b)
print(a>=b)


# 31 relational operator
a = 21
b = 30

print(a<b)
print(a<=b)
 
# 32 chaining operator
a = 22
b = 21
c = 12
print(a<b<c)
print(a>b<c)

# 33 string 
s = 'Anvesh'

# 34 string
s = "Anvesh"

# 35 string
s = """
    My name is anvesh
    my age is 22
"""

# 36 string
s = '''
    My name is anvesh
    my age is 22
'''

# 37 find method in string
s = "anvesh"
print(s.find('a'))

# 38 find method in string
s = "anvesh"
print(s.find("z"))


# 39 swapcase method in string
s = "anvesh"
print(s.swapcase())

# 40 upper method in string
s = "anvesh"
print(s.upper())

# 41 lower method in string
s = "anvesh"
print(s.lower())

# 42 capitalize mehtod in string
s = "anvesh"
print(s.capitalize())

# 43 title method in string
s = "anvesh"
print(s.title())

# 44 split method in string
s = "anvesh"
s = s.split()

# 45 join menthod in string
s = "anvesh"
s = s.split()
s ="-".join(s)

# 46 string slicing
s = "anvesh"
print(s[-1])
print(s[::-1])

# 47 range
for i in range(1,10):
    print(i)

# 48 range increment by 2
for i in range(1,20,2):
    print(i)

# 49 range using negitive numbers and backword direction
for i in range(-1,-20,-1):
    print(i)

# 50 range to print negitive numbers
for i in range(-20,1):
    print(i)


# 51 list comprehension to get a to z
l = [ chr(i) for i in range(ord('a',ord('z')+1))]
print(l)

# 52 list comprehension to get A to Z
l = [ chr(i) for i in range(ord('A'),ord('Z')+1) ] 
print(l)

# 52 to get even numbers
l = [ i for i in range(100,0,-1) if i%2 == 0]
print(l)

# to get even numbers in reverse
l = [ i for i in range(100,0,-2)]
print(l)

 
# 53 to get squares in dict comprehensions
d = { k:k*k for k in range(1,15) }
print(d)

# 54 set comprehensions
s = { i for i in range(0,100,2)}
print(s)

# 55 to get prime numbers in range O(n)
def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

l = [ i for i in range(2,100) if isPrime(i)]
print(l)


# 56 prime numbers in range O(n**1/2)
def isPrime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i == 0:
            return False
    return True

l = [ i for i in range(2,100) if isPrime(i)]
print(l)


# 57 fibonacci serise O(n)
def Fibo(n):
    
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    a = 0
    b = 1
    l = [a,b]
    for i in range(n):
        z = a + b
        a = b
        b = z
        l.append(z) 
    return l

l = Fibo(100)
print(l)


# 58 Fibo using reccursion
def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n-1) + fibo(n-2)

l = [ fibo(i) for i in range(0,25) ]
print(l)

# 59 int to bool,oct,hex
i = 10
print(bin(i))
print(oct(i))
print(hex(i))

# 60 bool to int,oct,hex
b = 0b1011
print(int(b))
print(oct(b))
print(hex(b))


# 61 oct to bool,int,hex
o = 0o172
print(bin(o))
print(int(o))
print(hex(o))

# 62 hex to bool,int,oct
h = 0x7ab
print(bin(h))
print(int(h))
print(oct(h))

# 63 to get power of two in range
def PowerOfTwo(n):
    if n&(n-1) == 0 :
        return True
    return False

l = [ i for i in range(1,100) if PowerOfTwo(i)]
print(l)

# 64 to get perfect squares with in range
def perfectSquare(n):
    res = n**0.5
    if res == int(res):
        return True
    return False

l = [ i for i in range(1,100) if perfectSquare(i)]
print(l)

# 65 to get perfect cubes with in range
def perfectCube(n):
    res = n**(1/3)
    if res == int(res):
        return True
    return False

l = [ i for i in range(1,100) if perfectCube(i) ]
print(l)

# 66 use case of chaining operation 
n = int(input("Enter amount to widthdraw between(100,25000): "))

if 100<n<25000:
    print(n,"/- amount widthdrawn")
else:
    print("enter amount within range of 100-25000")


# 67 filter products using chaining operation
products = { 'bag': 1500, 'book': 259, 'pen': 50, 'charger': 900, 'shirt': 700,
             'laptop': 45000, 'notebook': 120, 'headphones': 2300, 'jacket': 2500, 
             'mouse': 800, 'keyboard': 1500, 'backpack': 1800, 'wallet': 600, 
             'sunglasses': 1200, 'watch': 4000, 'shoes': 3200
            }

min_range = int(input("enter min range if not -1 : "))
max_range = int(input("Enter max range if not -1 : "))

print("products in range",min_range,max_range,"is")

for k,v in products.items():
    if max_range == -1 and v>= min_range:
        print(k,":",v)
    elif min_range == -1 and v < max_range:
        print(k,":",v)
    # chaining operator
    elif min_range <= v < max_range:
        print(k,":",v)

# 68 dict 
d = {'Anvesh':[22,30000], 'Surya':[21,39999], 'sunder':[23,40000]}
for k,v in d.items():
    s = f'EmpName: {k} age :{v[0]} sal :{v[1]}'
    print(s)

# 69 string
s = "Anvesh"
for i in s:
    print(i+"-",end="")

# 70 sort the charecters in string
s = 'Anvesh'
s = list(s)
s.sort()
s = "".join(s)
print(s)

# 71 to print assci values of a charecter
s = 'abcde'
l = [ ord(i) for i in s.upper()]
print(l)

# 72 fibonoci using dynamic programming
d = {}
def fibo(n):
    if n in d.keys():
        return d[n]
    if n == 1:
        return 1
    if n == 0:
        return 0
    d[n-1] = fibo(n-1)
    d[n-2] = fibo(n-2)
    return d[n-1] +d[n-2]

l = [ fibo(i) for i in range(0,25)]

print(l)


# 73 palindrome using slicing
def checkPali(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

s = input("enter a string : ")
print("Pali") if checkPali(s) else print("Not pali")


# 74 palindrome using while loop
def checkPali(s):
    s = s.lower()
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

s = input("enter a string : ")
print("Pali") if checkPali(s) else print("Not pali")

# 75 check palindrom using for loop
def checkPali(s):
    s = s.lower()
    l = len(s)-1
    for i in range(l//2+1):
        if s[i] != s[l-i]:
            return False
    return True

s = input("enter a string : ")
print("Pali") if checkPali(s) else print("Not pali")

# 76 replace method in string
s = "Anvesz"
s = s.replace('z','h')
print(s)

# 77 add an element in tuple using type casting
t = (1,2,3,4,5,6)
l = list(t)
l.append(7)
t = tuple(l)
print(t)

# 78 sort by removing duplicates
l = [6,3,3,1,3,5,6,7,1,5,4]
l =sorted( list( set(l)))
print(l)

# 79 sort in reverse
l = [6,3,3,1,3,5,6,7,1,5,4]
l.sort(reverse=True)
print(l)

# 80 return nth largest element
l = [6,3,3,1,3,5,6,7,1,5,4]
def nthLargest(l,n):
    s = sorted(set(l))
    if len(s) < n:
        return None
    return s[-n]
print(nthLargest(l,3))
print(nthLargest(l,10))

# 81 nested dict
e1 = {
    'name' : 'anvesh',
    'age' : 22,
}
e2 = {
    'name' : 'surya',
    'age' : 21,
}
e3 = {
    'name' : 'sunder',
    'age' : 23,
}
d = { 1 : e1, 2 : e2 , 3 : e3}
for k,v in d.items():
    print("empid : "+k,end=" : ")
    for i,j in v.items():
        print(f'{i} : {j}',end=", ")
    print()


# 82 strip in strings
message1 = "         hello how are you"
message2 = """



    good night sweet dreams take care             


"""
message3 = "What are you doing...                   "

print(message1)
print(message2)
print(message3,"String end")

print()

message1 = message1.lstrip()
print(message1)

# 83
message2 = message2.strip()
print(message2)

# 84
message3 = message3.rstrip()
print(message3,"String end")



# 85 F string (formatted string)
name = "anvesh"
age = 22

print("My nane is",name,"and my age is",age)

# 86
print(f"My name is {name} and my age is {age}")

# 87
print("My name is {} and my age is {}".format(name,age))

# 88 tokenize a string
message1 = message1.split()

for i in message1:
    print(i)


# 89 join a string
message1 = " ".join(message1)
print(message1)


# 90 time module to print seconds
import time 
print("time module is imported")

for i in range(0,10):
    print("time",i)
    time.sleep(1)
print("time out")

# 91 bytes 
l = [123,250,125,98]

encrypted = bytes(l)
print("encrypted list : ",encrypted)
print("decrypted list : ",*encrypted)

# 92 decrypting byte
for i in encrypted:
    print(i,end=", ")


# 93 byte array
l = [1,2,3,4,5,6,7,8]

encrypted = bytearray(l)
print("encrypted list : ",encrypted)
print("decrypted list : ",*encrypted)

# 94 add in element in byte array
encrypted.append(9)
print("encrypted list : ",encrypted)
print("decrypted list : ",*encrypted)

# 95 chaeck is it a valid identifier
def isValidIdentifier(s):

    import keyword
    if s in keyword.kwlist:
        return False

    s = list(s)

    if s[0].isnumeric():
        return False


    for i in s:
        if '_' == i:
            continue
        if i.isalnum():
            continue
        return False
    
    return True

s = input("enter a variable name : ")
print(f"{s} is applicable") if isValidIdentifier(s) else print("not possible")

# 96 is and is not
l = ['Anvesh']
s = 'Anvesh'
print(s is l[0])
print(s is not l[0])

# 97 adding elements from argv
from sys import argv
print(argv)
s = 0
for i in argv[1:]:
    s+=int(i)
print(s)

# 98 to get power of 2s using left shift
l = [ 1<<i for i in range(0,11)]
print(l)

# 99 to get power of 2s using right shift
l = [ 1024>>i for i in range(0,11) ]
print(l)

# 100 root of a number with in range
l = [ round(i**0.5,3) for i in range(1,11) ]
print(l)


# 101 done
course = "Python Full stack with AI"
institute = "IHub QualityThougt"
teacher = "Mr Abdhulla sir"
Girlfriend ="prerana"
Bestfriend = "Anvesh"
num = 100

res = f'successfully completed {num+1} programs \n{course} in institute {institute} trained by {teacher}'
print(res)

