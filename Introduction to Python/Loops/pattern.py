n = 6
 
prev = [[1]]

for i in range(1,n+1):

    for j in range(n-i):
        print(" ",end="")

    a = prev.pop()
    z = []

    for j in range(i):
        if j == 0 or j==i-1:
            print(1,end=" ")
            z.append(1)
        else:
            print(a[j]+a[j-1],end=" ")
            z.append(a[j]+a[j-1])  

    print()
    prev.append(z)