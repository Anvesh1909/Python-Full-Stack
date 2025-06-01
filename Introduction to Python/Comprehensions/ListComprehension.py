
# one expresion with one conditon
l1 = [ x*x for x in range(1,11)]

for i in l1:
    print(i,end=" ")

print()

# one expression with 2 condition
l2 = [ x*x for x in range(1,11) if x%2 == 0] 

for i in l2:
    print(i,end=" ")

# two expressions with one condition
l2 = [ x*x for x in range(1,11)] 







emptyList  = [None for i in range(10)]
print(emptyList)


even = [ i for i in range(50,101) if i%2 == 0]
print(even)

alphabets = [ chr(i) for i in range(65,65+26)]
print(alphabets)

name = "anvesh"
charecters = [ i for i in name]
print(charecters)

sentance = '''python supports comprehension methodology. 
it can be represent as if we are using one or more than one expresion with 
one or more than one condition then it is said to be comprehension in python
'''

words = [ word for word in sentance.split(" ")]

print(words)

words = sentance.split()
print(words)



nums = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

num = [j for i in nums for j in i]

print(num)