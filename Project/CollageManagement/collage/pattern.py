n = 5
 
prev = [[1]]

for i in range(1,n+1):
    a = prev[-1]
    z = []
    for j in range(1,i+1):
        if j == 1 or j==i:
            print(1,end=" ")
            z.append(1)
        else:
            print(a[j]+a[j-1],end=" ")
            z.append(a[j]+a[j-1])  
    print()
    prev.append(z)

