# 1 
i = 1
while i<=10:
    print(i)
    i+=1


# 2
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# 3
n = 10
s = 0 
for i in range(1,n+1):
    s+=i
print(s)


# 4
num = 2
for i in range(1,11):
    print(num*i)

# 5
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>150:
        if i>500:
            break
        continue
    if i%5==0:
        print(i)


# 6
n = 75869
c = 0
while n>0:
    c+=1
    n//=10
print(c)

# 7
n = 5
for i in range(n):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()


# 8
list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
    print(i)
 


# 9
for i in range(-10,0):
    print(i)


# 10
for i in range(1,5):
    print(i)
else:
    print("Done!")


# 11
start = 25
end = 50

for n in range(start,end+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)


# 12
n = 10

a = 0
b = 1

print("Fibonacci sequence:")
print(a,b,end=" ")
for i in range(n-2):
    c = a+b
    a = b
    b = c
    print(c,end=" ")


# 13
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))


# 14
n = 76542
rn = 0
while n>0:
    a = n%10
    rn = rn*10+a
    n //=10
print(rn)


# 15
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 1
while i<len(my_list):
    print(my_list[i],end=" ")
    i+=2
    

# 16
n = 6
for i in range(1,n+1):
    print(f"Current Number is: {i} and the cube is {i**3} ")


# 17
a = 2
n = 5
s = 0
for i in range(n):
    s+= a
    a = a*10 + 2

print(s)


# 18
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("* ",end="")
    print()

