def listOfPrime(n):

    def Prime(n):
        for i in range(2,n//2):
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

    L = list(l)

    def min(l):
        m = 0
        for i in l:
            if m > i:
                m= i
        return m

    sortedL = []

    for i in range(len(L)):
        sortedL.append()


