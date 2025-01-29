# 1
i = 0 
while i<11:
    print(i)
    i+=1


# 2
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    

# 3
n = int(input("Enter a number: "))
s = 0
for i in range(1,n+1):
    s+=i
print("Sum is:",s)




# 4
num = int(input("Enter a number: "))
for i in range(1,11):
    print(num*i)
    
    
    
# 5
numbers = [12, 75, 150, 180, 145, 525, 50] 
def check(nums):
    for i in nums:
        if i%5==0 and i<=150:
            print(i)
        if i>500:
                break
            
check(numbers)




# 6
n = 75869
c=0
while n>0:
    n//=10
    c+=1
print(c)
    





# 7
n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
    
    

# 8
list1 = [10, 20, 30, 40, 50] 
i = len(list1)-1
while i>=0:
    print(list1[i])
    i-=1



# 9
for i in range(-10,0):
    print(i)
    
    
    
# 10
for i in range(5):
    print(i)
else:
    print("Done!")
    
    
    
# 11
start = int(input("Enter Start Value: "))
end = int(input("Enter End Value: "))

for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        
        
        
        
# 12
n = int(input("Enter a number: "))
a = 0
b = 1
print(a,b,end=" ")
for i in range(n-2):
    c = a+b
    print(c,end=" ")
    a = b
    b = c
    
    
    

# 13
n = int(input("Enter a number: "))
fact = 1
for i in range(n,0,-1):
    fact *= i
print(fact)






# 14
n = 76542
rn = 0
while n>0:
    a = n%10
    rn= rn*10+a
    n//=10
print(rn)





# 15
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 1
while i<len(my_list):
    print(my_list[i],end=" ")
    i+=2
    
    
    
# 16
n = int(input("Enter a numeber: "))
for i in range(1,n+1):
    print(f"Current Number is: {i} and the cube is {i**3}")
    
    
    
    
# 17
n = 5
a = 2 
s = 0
for i in range(n):
    s+=a
    a = a*10 +2
print(s)




# 18
n = 6
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
    
    
# 19

n = int(input("Enter a number: "))
if n%2==0:
    if n<0:
        sign = "negitive"
    else:
        sign = "positive"
    num = "even"
else:
    num = "odd"
    if n<0:
        sign = "negitive"
    else:
        sign = "positive"


print(f"the given number is {sign} and {num} number")
    




# 20
n = 5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
    
    
    
# 21
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(max(i,j),end=" ")
    print()
        


# 22
n = 8
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
    
    
    
    
# 23
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
    
    
    
# 24
n = 5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()
    
    
    
# 25
n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
    


