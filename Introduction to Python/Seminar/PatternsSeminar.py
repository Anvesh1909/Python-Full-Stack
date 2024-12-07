n = int(input("Enter  a number: "))

for i in range(1,n+1):
    print(i,end="")




n = int(input("Enter  a number: "))

for i in range(1,n+1):
    print("*"*i)



n = int(input("Enter  a number: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()



n = int(input("Enter  a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
    

n = int(input("Enter  a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()



n = int(input("Enter  a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()



n = int(input("Enter  a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()



n = int(input("Enter  a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()