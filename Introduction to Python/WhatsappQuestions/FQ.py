# 1> Create a function to find nth largest number from the list l=[4,2,0,9,7,3,2,11] without using builtin functions.


def NthLargest(L,n):
    Largest = []
    for i in range(n):
        m = 0
        for i in L:
            if i not in Largest and m < i:
                m = i

        Largest += [m]
    return Largest[n-1]

L = [2,1,6,2,1,4,5]
print(NthLargest(L,3))
print(NthLargest(L,2))




# 2> convert string of numbers into integer format without using typecasting ?
def convertInterger(s):
    I = {
        "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9
    }

    n = 0
    for i in s:
        n = n*10 + I[i]
    return n

n = input("Enter a Number: ")
print(type(n))
n= convertInterger(n)
print(n)
print(type(n))



# 3> You are given an integer list 'ARR' of size 'N' and an integer 'S'.
#  Your task is to return the list of all pairs of elements such that 
#    each sum of elements of each pair equals 'S'.
   
#    input:- arr = [1,2,3,4,5,6]
#         s=7

#    output :- [(3, 4), (2, 5), (1, 6)]


arr = [1,2,3,4,5,6]
s=7

res = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == s:
            res.append((arr[i],arr[j]))

print(res)


# 4> find the prime numbers between given range using lambda function ?

#    input :- enter start point:- 8
#          enter end point:- 20

#    output :- [11, 13, 17, 19]


start = int(input("enter start: "))
end = int(input("enter end: "))

prime = lambda a: ([i for i in range(2,a) if a%i==0] == [])


for i in range(start,end):
    if prime(i):
        print(i)



# 5> Input a string having some digits. Write a function to return the sum of digits present in this string
# [hint :- use isalnum()]

s = input("Enter a number : ")

sumOfNums = 0

for i in s:
    if i.isdigit():
        sumOfNums += int(i)

print(sumOfNums)
