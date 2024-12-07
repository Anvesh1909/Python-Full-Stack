n = int(input("Enter a number : "))

for i in range(1,n+1):
    print(i)

for i in range(1,n+1):
    print("*"*i)

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()


n = int(input("Enter a number : "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i)


for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()


n = int(input("Enter a number : "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()





n = int(input("Enter a number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


n = int(input("Enter a number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()
