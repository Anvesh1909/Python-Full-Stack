# 1. Write a python code to perform sum of squares of [2,4,6,8] using lambda function.

from functools import reduce
L = [2,4,6,8]
res = reduce(lambda a,b:a+b,map(lambda a:a*a,L))
print(res)

# 2. Can u perform the product for each elements to the [3,5,10,6] using lambda function.
#   output : 900 (:>3*5*10*6)

from functools import reduce
L = [3,5,10,6]
res = reduce(lambda a,b: a*b,L)
print(res)

# 3. Write a python code to validate filter(),map(),reduce() using lambda (Anonymous) function.

L = [i for i in range(1,11)]

print("Square all numbers")
print(list(map(lambda a:a*a,L)))

print("Filter even Numbers")
print(list(filter(lambda a: a%2==0,L)))

from functools import reduce
print("add all numbers")
print(reduce(lambda a,b:a+b,L))

# 4. Retrieve the even numbers only that should be greater than 300 and it's length should be 3 
# only from the list nums=[810,2, 1555,15, 720, 425, 130,13, 350] using lambda function.

nums=[810,2, 1555,15, 720, 425, 130,13, 350]

L = lambda a: a%2==0 and a>300 and a<=999 

res = list(filter(L,nums))
print(res)


# 5. Retrieve the Strings from the list that should start with digits using lambda function.

SList = ["Anvesh","122Bunny","211Lisb","aidc"]
L = lambda a: a[0] in "0123456789"
res = list(filter(L,SList))
print(res)

# 6. Check prime number using lambda function.

n = int(input("enter a number: "))

L = lambda n : [i for i in range(2,int(n**0.5)+1) if n%i==0 ] == []
if L(n) : print(n,": is a prime number")
else : print(n,":is not a prime number")
