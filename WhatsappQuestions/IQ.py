
# 1. Write a function that computes the area of a triangle given the base and height as parameters.

def areaOfTriangle(b,h):
    return 0.5*b*h

print(areaOfTriangle(4,5))


# 2. Write and test a function to meet this specification. squareEach (nums) nums is a list of numbers. Modifies the list by squaring each entry.

L = [5,3,2,4,6,7,3]
sq = lambda a:a*a
def test(a):
    return a*a
print(list(map(test, L)))

# 3. Write and test a function to meet this specification. sumList (nums) nums is a list of numbers. Returns the sum of the numbers in the list.
from functools import reduce

L = [5,3,2,4,6,7,3]
sum = lambda a,b : a+b
print(reduce(sum,L))

# 4. Write and test a function to meet this specification. toNumbers (strList) strList is a list of strings, 
# each of which represents a number. Modifies each entry in the list by converting it to a number.

strList = ['1','2','3','4']

def toNumber(n):
    d = { f"{i}":i for i in range(10)}
    return d[n]

n = 0
for i in strList:
    n = n*10 + toNumber(i)

print(n)

# 5. Parameters are an important concept in defining functions. 
#    a) What is the purpose of parameters? 
#   b) What is the difference between a formal parameter and an actual parameter? 
#   c) In what ways are parameters similar to and different from ordinary variables?



