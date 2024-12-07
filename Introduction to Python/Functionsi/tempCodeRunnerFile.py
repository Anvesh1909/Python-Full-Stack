
BubbleSort(11,40,20,2,4,12,42)


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

        