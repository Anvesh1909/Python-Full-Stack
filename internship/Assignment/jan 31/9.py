# 1
l1 = list(("Rose","Peony","Orchids","Snowdrop","Calendula","Aster","Tulips","Bluebell","Sunflower"))
l2 = ["Rose","Peony","Orchids","Snowdrop","Calendula","Aster","Tulips","Bluebell","Sunflower"]
print(l1)
print(l2)


# 2
l1 = ["Rose","Peony","Orchids","Snowdrop","Calendula","Aster","Tulips","Bluebell","Sunflower"]
def length(L):
    l = 0
    for _ in L:
        l+=1
    return l
print(length(l1))


# 3
def length(L):
    l = 0
    for _ in L:
        l+=1
    return l
l = ["Anvesh",22,55000.00,True,2+5j]
print(length(l))



# 4
l = ["Anvesh",22,55000.00,True,2+5j]
print(l[::-1])



# 5
list1 = ["Hello","take"]
list2 = ["Dear","Sir"]
res = list1+list2
print(res)


# 6
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)



# 7
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)



# 8
list1 = [5, 10, 15, 20, 25, 50, 20] 
i = 0 
while i<len(list1):
    if list1[i] == 20:
        break
    i+=1
list1[i]=200
print(list1)




# 9
l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
i = 0 
res = []
while i<len(l):
    if i not in [0,4,5]:
        res += [l[i]]
    i+=1
print(res)



# 10
l1,l2 = [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]  
res = l1[:-1]+l2
print(res)



# 11
l1,l2 = [10, 20, 30],[40, 50, 60] 
for i in l1:
    l2 += [i]
print(l2)



# 12
Number = [10, 20, 30, 40]  
animal = ["Cat", "Dog", "Lion", "Panda"]
res = Number + animal
print(res)




# 13
'''
Ordered: Lists maintain the order of items.

Mutable: Items can be changed after the list is created.

Allow Duplicates: Lists can contain the same item multiple times.

Heterogeneous: Lists can contain items of different data types.
'''


# 14
'''
using square brackets or list() prebuilt function
'''


# 15
'''
using indexing
slicing
negitive indexing
'''



# 16
'''
using indexing
'''
animal = ["Cat", "Dog", "Lion", "Panda"]
print(animal[0])
print(animal[1])
print(animal[2])
print(animal[3])



# 17
animal = ["Cat", "Dog", "Lion", "Panda"]
print(animal[::2])


# 18
animal = ["Cat", "Dog", "Lion", "Panda"]
'''using length function'''
print(len(animal))



# 19
'''
A list in Python is a collection of items that are ordered and changeable. 
It is defined using square brackets [].
'''



# 20 
'''
using append 
insert
extends
'''
