# 1
keys = ['Ten', 'Twenty', 'Thirty']  
values = [10, 20, 30] 

d = {k:v for k,v in zip(keys,values)}
print(d)



# 2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}  
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)




# 3
sampleDict = {  
    "class": {  
        "student": {  
            "name": "rajvamshi",  
            "marks": {  
                    "physics": 70,  
                    "history": 80  
            }  
        }  
    } 
}


print(sampleDict['class']['student']['marks']['history'])




# 4
employees = ['Kelly', 'Emma']  
defaults = {"designation": 'Developer', "salary": 8000} 

d = {}
for i in employees:
    d[i] = defaults
print(d)



# 5
d = {"Name": "Ram", "Age": 23 }
print(d)
d['City']='Salem'
print(d)
d['Gender']='Male'
print(d)



# 6
d1= {"Name": "Ram", "Age":23}  
d2= {"City": "Salem", "Gender": "Male"}  
d3= {"Mark":450}  
d4= {}

res = {**d1,**d2,**d3,**d4}
print(res)





# 7
d1= {"Name": "Ram", "Age":23}  
d2= {"City": "Salem", "Gender": "Male"}
res = {**d1,**d2}
print(res)





# 8
d  = {1:23, 2:45, 3: -17, 4:87}
print(sum(d.values()))



# 9
student = {"Name": "Pooja", "Age":23, "Gender": "Female", "City": "Salem", "Mark":488} 
for i in student.keys():
    print(i)




# 10
student = {'name': 'Ram', 'age': 23, 'city': 'Salem',"name" : "Bunny"}
print(student) 




# 11
keys = ["One", "Two", "Three", "Four", "Five"]  
values = [1, 2, 3, 4, 5]

d = {k:v for k,v in zip(keys,values)}
print(d)




# 12
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"} 
keys = list(sample_dict.keys())[::2]
print("Keys = ",keys)
res = {k:sample_dict[k] for k in  keys}
print(res)





# 13
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
keys = ["name", "salary"] 
for i in keys:
    sample_dict.pop(i)
    # sample_dict.popitem()
print(sample_dict)




# 14
sample_dict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New York"} 
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)



# 15
sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
print(list(sample_dict.keys())[1])



# 16
sample_dict = {  
    'emp1': {'name': 'Jhon', 'salary': 7500},  
    'emp2': {'name': 'Emma', 'salary': 8000},  
    'emp3': {'name': 'Brad', 'salary': 500}  
}

sample_dict["emp3"]["salary"] = 8500
print(sample_dict)




# 17
d = {}
d["name"] = "Anvesh"
d["Age"] = 22
print(d)




# 18
sample_dict = {  
    'emp1': {'name': 'Jhon', 'salary': 7500},  
    'emp2': {'name': 'Emma', 'salary': 8000},  
    'emp3': {'name': 'Brad', 'salary': 500}  
}

sample_dict.pop("emp3")
print(sample_dict)




# 19
sample_dict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New York"} 
print(max(sample_dict))
print(min(sample_dict))
print(len(sample_dict))
print(all(sample_dict))
print(any(sample_dict))
print(type(sample_dict))

