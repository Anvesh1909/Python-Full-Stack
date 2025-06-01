def listOfPrime(n):

    def Prime(n):
        for i in range(2,int(n**2)+1):
            if n%i== 0:
                break
        else:
            print(n)
        
    for i in range(1,n+1):
        Prime(i)

listOfPrime(100)





def BubbleSort(*a):

    a = list(a)

    def Swap(i,j):
        a[i],a[j] = a[j], a[i]

    max = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                Swap(j,j+1)

    print(a)

BubbleSort(11,40,20,2,4,12,42)
        


def SelectionSort(*L):

    L = list(L)

    def min(l):
        m = 0
        for i in l:
            if m > i:
                m= i
        return m

    sortedL = []

    for i in range(len(L)):
        sortedL.append()








# 1 1 2 3 5 8 13...
def fibonicci(n):
    a = 1
    b = 1 
    print(a,b,end=" ")
    for i in range(n-2):
        c = a+b
        print(c ,end=" ")
        a = b
        b = c


fibonicci(10)


def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(5))











t= ([1,2,3,4],7,8,9)
print(t)

l = t[0].copy()
print(l)

l.append(5)
print(l)
print(t)




t= ([1,2,3,4],1,2,3)

print(t[0][1])