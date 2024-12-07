print("*"*1)
print("*"*2)
print("*"*3)
print("*"*4)



# for i in range(1,n+1):
#     print("*"*i)

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()



n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n):
        print("*",end="")
    print()



n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()



n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()



n = int(input("Enter a number: "))

for i in range(1,n+1):
    # print(" "*(n-i),end="")
    for j in range(n-i):
        print(" ",end="")
    
    for j in range(i):
        print("*",end="")
    print()



n = int(input("Enter a number: "))


for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()



n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()



n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()



n = int(input("Enter a number: "))

a = ord("A")

for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(a),end=" ")
        a+=1
    print()


n = int(input("Enter a number: "))

for i in range(n,0,-1):
    for j in range(n-i+1):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()



n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1 or i == n or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
     
        

n = int(input("Enter a number: "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        if j == 1 or i == n or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
     



n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        if j == 1 or i == n or i==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print(" Hello I am "'Anvesh'" from ")