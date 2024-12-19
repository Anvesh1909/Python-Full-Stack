n = 4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()




n = 6
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()




n = 5

for i in range(1,n+1):
    for j in range(i):
        print("*",end= "")
    print()



n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        if j ==1 or i==n or i==j:
            print("*",end= "")
        else:
            print(" ",end="")
    print()





n = 6

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==j or j==1 or i==n:
            print("* ",end="")
        else:
            print("  ",end="")
    print()



n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j-1==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()