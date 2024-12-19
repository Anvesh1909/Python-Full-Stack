# 1. Write a python code to generate the following output using CLA.
#   Output : 'George' 'Bush'


from sys import argv

# print(argv)

# python BQ1.py "'George'" "'Bush'"

for i in argv[1:]:
    print(i,end=" ")




# 2. Write a python code to display the output as follows using the elements 5,-3,9,0,7,2 in CLA.
#   Output : [-3,0,2,5,7,9]



# python BQ2.py 5,-3,9,0,7,2

from sys import argv

# print(argv)

l = argv[1].split(",")
l = [ int(i) for i in l]

l.sort()
print(l)





# 3. Show the output as follows by using CLA.
#   Output: 2-4-6-8-10-

# python BQ3.py 2 4 6 8 10

from sys import argv

res = ''
for i in argv[1:]:
    res += i + "-"

print(res)




# 4. Findout the sum of the elements from the user input using CLA.

# python BQ4.py 2 4 6 8 10

from sys import argv

s = 0
for i in argv[1:]:
    s += int(i)

print(s)








# # 5. Check whether the number is a 7 multiple or not,
# # if it is 7 multiple then check that exists in the multiples=[33,49,35,24,45] or not using CLA.


from sys import argv

exists = False

for i in argv[1]:
    if int(i) % 7 == 0 :
        exists = True
        break

print("exists" if exists else "not exists")