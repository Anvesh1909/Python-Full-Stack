
# common for loop
l1 = [11,17,16,12,14,13,79,89,91,92,1005,1006,1007,1008]

for i in range(len(l1)):
    if l1[i] <20:
        l1[i] += 500
    elif l1[i]>1000:
        l1[i] += 600

print(l1)

# print multiples of a number
t = int(input("Enter a number"))

for i in range(1,10+1):
    print(f"{t} X {i} = {t*i}")


# print nth largest number 
l = eval(input("Enter the list: "))

l = sorted(l)

n = int(input("Enter nth largest : "))

print(l[-n])

l = sorted(l,reverse=True)

print(l[n-1])




# nth largest element using for loop 
l = eval(input("Enter the list: "))

n = int(input("Enter nth largest : "))

largest = []

for i in range(n):
    m = 0
    for j in l:
        if m<j and j not in largest:
            m = j
    largest.append(m)

print(largest[-1])



# count vowels in a string
c=0

for s in input("Enter a string : "):
    if s in "AEIOUaeiou":
        c+=1

print(c)



# reversing a string
origi = input("Enter a string : ")
rever = ""

for i in origi:
    rever = i + rever

print(rever)


# checking a string is palindrine or not 
origi = input("Enter a string : ")
rever = ""

for i in origi:
    rever = i + rever

if origi == rever: print("palindrome")
else : print(origi,rever,"Not a palindrome")



# printing a string
s = input("Enter a string")

for i in s:
    print(i)
for j in s:
    print(j,end=" ")



# palindrome number
n = int(input("Enter a number : "))
digits = 1
temp = n

while temp > 9:
    digits*=10
    temp//=10

rn = 0
temp = n

while temp >0:
    a = temp % 10
    rn+=digits*a
    temp//=10
    digits//=10

print(n,rn,"is",n == rn)





# fibonocii serise
n = int(input("Enter a  number : "))
if n == 1:
    print(0)
elif n== 2 :
    print(0,1)
else:
    print(0,1,end=" ")
    a = 0
    b = 1
    for i in range(2,n):
        z = a+b
        a = b
        b = z
        print(z,end=" ")



# amstrong number
n = int(input("Enter a number: "))

digit = 0
temp = n
while temp > 0:
    digit+=1
    temp //=10

temp = n
sum = 0
while temp > 0:
    a = temp%10
    sum += a**digit
    temp//=10

print(n,sum,"is amstrong number",sum == n)





# check two string is annagram or not
s1 = input("Enter a strig: ")
s2 = input("Enter another string: ")

s2 = list(s2)

for i in s1:
    if i in s2:
        s2.remove(i)
    else:
        break

if len(s2)==0:
    print("Annagram")
else:
    print("not an annagram")





# example 1
for i in range(3):
    print(i)
    for j in range(3):
        print(j)





# exaple 2
L = [['A','B','C'],['D','E','F'],['G','H','I']]


for i in L:
    print(i)
    for j in i:
        print(j)

print()

for i in L:
    for j in i:
        print(j)

print()

for i in L:
    for j in i:
        print(j,end=" ")

print()
print()

for i in L:
    for j in i:
        print(j,end=" ")
    print()









# mul = []

# for i in range(1,11):
#     a = []
#     for j in range(1,8):
#         x=f"{j}X{i}={i*j}"
#         a.append(x)
#     mul.append(a)

# for i in zip(i for i in mul):
#     for j in i:
#         print(j,end=" ")
#     print() 


# display 1:7 table all table must inn one row
# method 1
for i in range(1,11):
    for j in range(1,8):
        print(f"{j}X{i}={i*j}",end=" ")
    print()


# method 2
for i in range(1,11):
    for j in range(1,8):
        if i<10 and i*j<10: 
            print(f"{j}X {i}= {i*j}",end=" ")
        elif i<10 and i*j<10:
            print(f"{j}X {i}= {i*j}",end=" ")
        elif i<10:
            print(f"{j}X {i}={i*j}",end=" ")
        else:
            print(f"{j}X{i}={i*j}",end=" ")
    print()



# method 3
for i in range(1,11):
    for j in range(1,8):
        s = f"{j}X{i}={i*j}"
        s = s + " "*(7-len(s))
        print(s,end=" ")
    print()








# write a python script perform transpose of the matrix usig nested forloop.
m = [[1,2,3],[4,5,6],[7,8,9]]

for i in m:
    for j in i:
        print(j,end=" ")
    print()

print()
print("Transpose = ")

for i in range(len(m[0])):
    for j in range(len(m)):
        print(m[j][i],end=" ")
    print()




# write a python script perform transpose of the matrix usig nested forloop.
r = int(input("enter number of rows : "))
c = int(input("enter number of cols : "))

matrix = []

for i in range(r):
    a = []
    for j in range(c):
        x = int(input(f"Enter M[{i+1}][{j+1}]= "))
        a.append(x)
    matrix.append(a)
    print()

for i in matrix:
    for j in i:
        print(j,end = " ")
    print()


t = []

for i in range(len(matrix[0])):
    a = []
    for j in range(len(matrix)):
        a.append(matrix[j][i])
    t.append(a)


for i in t:
    for j in i:
        print(j,end = " ")
    print()








# write a python script perform matrix multiplcation using nested forloop.
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[1,2,3],
     [4,5,6],
     [7,8,9]]

res = [ [ 0 for i in range(len(A[0])) ] for j in range(len(A)) ]


for i in range(len(A)):
    for j in range(len(A[0])):
        mul = 0
        for k in range(len(A)):
            mul += A[i][k] * B[k][j]
        res[i][j] = mul

for i in res:
    for j in i:
        print(j,end=" ")
    print()




# 1 is prime method 1
n = int(input("enter a prime number = "))
isPrime = True

for i in range(2,n):
    if n%i == 0:
        isPrime = False
        print("is not prime")
        break


    
if isPrime == True:
    print(n," is prime number")
else:
    print(n," is not prime number")






# 2 is prime method 2
n = int(input("enter a prime number = "))
isPrime = True


for i in range(2,n//2):
    if n%i == 0:
        isPrime = False
        print("is not prime")
        break
    

if isPrime == True:
    print(n," is prime number")
else:
    print(n," is not prime number")



# 3 is prime method 3
n = int(input("enter a prime number = "))
isPrime = True


for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        isPrime = False
        print("is not prime")
        break
    

if isPrime == True:
    print(n," is prime number")
else:
    print(n," is not prime number")



# 4 print all prime and composite in range
prime = []
composite = []

for i in range(1,51):
    isPrime = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            isPrime = False
    prime.append(i) if isPrime else composite.append(i)

print(prime)
print(composite)




# 4 bubble sort
L = [5,2,4,1,3]

for i in range(len(L)):
    m = 0
    for j in range(len(L)-i):
        if L[m] < L[j]:
            m = j
    x = L[j]
    L[j] = L[m]
    L[m] = x

print(L)


# 5 selection sort
L = [4,5,3,2,1]

for i in range(len(L)):
    for j in range(len(L)-i-1):
        if L[j] > L[j+1]:
            L[j],L[j+1] = L[j+1],L[j]

print(L)


# 6 pyramid
n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()


# 7 print all ids in dictionary
d = {1:"Anvesh",2:"Surya",3:"sunder"}

for k in d.keys():
    print(f"hello good morning {d[k]}")

            


    



col = ["Eid","Name","sal"]
Eid = [1,2,3]
name = ["ANvesh","surya","Sunder"]
sal = [2022,1332,2564]

# n = int(input("enter the number of records: "))

# for i in range(n):
#     Eid.append(int(input(f"enter id {i+1} = ")))
#     name.append(input(f"enter name {i+1} = "))
#     sal.append(float(input(f"enter dal {i+1} = ")))

# print(Eid)
# print(name)
# print(sal)

values = list(zip(Eid,name,sal))

t = dict(zip(col,values))

# print(t)

for k in t.keys():
    print(f"| {k} |",end="")

print()

for v in t.values():
    for i in v:
        print(f"| {i}  |",end="")
    print()







l = eval(input("Enter  a list : "))
n = int(input("Enter a number : "))

for i in l:
    if i == n:
        print(f"Number {n} excits ")
        break
else:
    print(f"number {n} not excits")





# 1. write a python script write an even logic display odd numbers 
for i in range(1,50):
    if i%2==0:
        continue
    print(i)



n = int(input("Enter a number less than = 50 : "))

for i in range(n):
    if i>= 50:
        print("Number is greater than 50")
        break
    if i%2==0:
        continue
    print(i)
else:
    print("Execution completed sussfully")





roll = [1,2,3,4,5,6,7]
present = [1,2,3,4]


for i in roll:
    if i in present:
        print(i,"Present")
        continue
    if i not in present:
        print(i,"Why your absent")
        break

    
    
