L=[[1,2,3],[4,5,6],[7,8,9]]
n=len(L)
i=0
res=[]
while i<n:
    g=[]
    j=n-1
    while j>=0:
        g+=[L[j][i]]
        j-=1
    res+=[g]
    i+=1

print(res)
