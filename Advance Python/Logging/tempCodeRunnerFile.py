from functools import reduce
L = [1,2,3,4,5]

# def add(a,b):
#     return a+b

add = lambda a,b: a+b
x = reduce(add,L)
print(x)