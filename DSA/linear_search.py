
def linerSearch(l,k):
    for i in range(len(l)):
        if l[i] == k:
            return i
    return -1



l = ['a','b','c','d','e','f','h']
k ='f'

result=linerSearch(l,k)
if result!= -1:
    print(f'Target element {k} found at index {result}')
else:
    print("element not found")




