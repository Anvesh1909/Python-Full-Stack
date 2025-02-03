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
set1.update(set1.intersection(set2))
print(set1)