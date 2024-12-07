from sys import *

# python CLA.py 100 200 300 400
print(argv)
print(type(argv))

print(argv[0])
print(argv[1])
print(argv[2])
 
res = ''
for i in argv[1:]:
    res+=i

print(res)

res = 0

for i in argv[1:]:
    res+= int(i)

print(res)