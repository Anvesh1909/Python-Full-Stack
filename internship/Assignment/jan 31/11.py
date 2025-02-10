# 1
sample_set = {"Yellow", "Orange", "Black"}  
sample_list = ["Blue", "Green", "Red"] 
for i in sample_list:
    sample_set.add(i)
print(sample_set)



# 2
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))




# 3
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70} 
print(set1.union(set2))




# 4
set1 = {10, 20, 30}  
set2 = {20, 40, 50}
print(set1.difference(set2))



# 5
set1 = {10, 20, 30, 40, 50}
r = {10,20,30}
print(set1.difference(r))




# 6
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70} 
u = set1.union(set2)
i = set1.intersection(set2)
print(u.difference(i))





# 7
set1 = {10, 20, 30, 40, 50}  
set2 = {60, 70, 80, 90, 10} 
print("Two sets have items in common",set1.intersection(set2))





# 8
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70} 

u = set1.union(set2)
i = set1.intersection(set2)
set1 = u.difference(i)
print(set1)





# 9
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70}
set1 = set1.intersection(set2)
print(set1)




# 10
s = set()
print(type(s))




# 11
s = set()
s.add(10)
s.add(20)
s.add(30)
s.add(10)
s.add(40)
s.add(50)
print(s)




# 12
s = {10,20,30,40,50}
s.remove(20)
print(s)





# 13
a = {30,40,70,20}  
b = {20,50,60,40} 
print(a.intersection(b))



# 14
a = {30,40,70,20}  
b = {20,50,60,40}
print(a.union(b))


# 15
a = {30,40,70,20,80,50}  
b = {20,50,60,40,90,10}
print("Difference of a - b:",a.difference(b))
print("Difference of b - a:",b.difference(a))
      
      
      
      
# 16
a = {30,40,70,20,80,50}  
b = {20,50,60,40,90,10}
print("symmetric_difference of a - b:",a.symmetric_difference(b))
print("symmetric_difference of b - a:",b.symmetric_difference(a))




# 17
X = {50, 20, 70, 40, 10, 60, 30}  
Y = {80, 50, 100, 70, 90, 60}

print("First Method using difference() ")
print("Difference of X - Y:",X.difference(Y))
print("Difference of Y - X:",Y.difference(X))

print("First Method using operator (-) ")
print("Difference of X - Y:",X-Y)
print("Difference of Y - X:",Y-X)





# 18
a = {23,45,78,8,56}  
b = {42,55,26,87}  
z = {87,46}

if a.intersection(b) == set():
    print("Compare A and B:",True)
else:
    print("Compare A and B:",False)
    
if b.intersection(z) == set():
    print("Compare B and Z:",True)
else:
    print("Compare B and Z:",False)
    
if a.intersection(z) == set():
    print("Compare A and Z:",True)
else:
    print("Compare A and Z:",False)
    
    
    

# 19
a = {23,45,17,8,56,10}
print("Set A:",a)
print("Maximum of A:",56)
print("Minimum of A:",8)




# 20
color = {"Red","Green","Pink","White","Black","Yellow","Blue"} 
color.clear()
print("After Removing all Elements give Sets:",color)




# 21
a = [1,2,3,4,5,6,7,8]  
b = [11,2,43,48,55,6,76,8]
print("X:",set(a))
print("Y:",set(b))
res = list(set(a).intersection(set(b)))
print("\nintersection of Two Lists:",res)





# 22
s = "QualityThought" 
print("String Value:",s)
print("String Converted to Set:",set(s))




# 23
S= {'Q', 'i', 'u', 'a', 't', 'y', 'i', 'T', 'h', 'o', 'u', 'g', 'h', 't'}
print("String Value",S)
print(type(S))
S = str(S)
print("Set Convert to String:",S)
print(type(S))




# 24
val = {'A', 'P', 'P', 'L', 'E'}
print("Convert Set into List",list(val)) 




# 25
val = {'A', 'P', 'P', 'L', 'E'}
print("Convert Set into Tuple",tuple(val)) 



# 26
val = ('A', 'P', 'P', 'L', 'E')
print("Convert tuple into set",set(val)) 



# 27
x = {10,20,30,40,50}  
y = [60,70,80,90,100]
print("X:",x)
print("Type of X:",type(x))
print("Y:",y)
print("Type of Y:",type(y))

for i in y:
    x.add(i)
print("Add all its Elements into a given set:",x)


# 28
x = {10, 20, 30, 40, 50}  
y = {40, 50, 60, 70,80} 
res = x.union(y)
print(res)




# 29
Set1 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}  
Set2 = {20, ('Python', 'C'), 10, 11, ('J', 'O', 'E')}
print("Union:",Set1.union(Set2))
print("Symmentic Difference:",Set1.symmetric_difference(Set2))
print("Intersection:",Set1.intersection(Set2))



# 30
s = {10,20,30,40,50} 
x = 15
y = 20
if x in s:
    print(True)
else:
    print(False)
if y in s:
    print(True)
else:
    print(False)