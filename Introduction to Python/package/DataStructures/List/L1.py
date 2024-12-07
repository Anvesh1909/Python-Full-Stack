def Slicing(L,start=0,end=0,step=1):
    if end == 0 :
        end = len(L)
    if start > end:
        step=-1
    return L[start:end:step]


l = [1,2,3,4,5,6,7]

print(Slicing(l,0,10,2))