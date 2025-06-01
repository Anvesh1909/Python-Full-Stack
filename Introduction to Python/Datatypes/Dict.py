d = {}
print(d)
print(type(d))

#  or

d = dict()
print(d)
print(type(d))


print()


d = {"Eid" : 1001, "Ename" : "Anvesh", "Esal" : 35000.50 }
print(d)
print(type(d))


d = {1: "Anvesh", 2: "Bunny"}
print(d)


d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}
print(d)

# to update dictionary
d['mdate'] = 2024
d['expdate'] = 2029

print(d)

print("pid is",d['pid'])
print("pname is",d['pname'])

# print(d['Anvesh'])


d = {1:1000, 2:2000, 3:3000}
print(d[1])
print(d)



d = dict()
print(type(d))
print(d)

d = dict(k1=1000, k2=2000, k3=3000)
print(d)



# functions in dict

d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}
print(d)

for k in d.keys():
    print(k)


print(d.keys())

for v in d.values():
    print(v)

print(d.values())
print(list(d.values()))


x = (10,20)
print(x) 
x,y = (10,20)
print(x,y)




d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}
print(d)

for k,v in d.items():
    print(k,v)
print(d.items())


# it will generate in form of tuple for each item

for i in d.items():
    print(i)


# deep copy
d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}

# dc = d
dc = d.copy()
print(dc)

d.clear()
print(d)
print(dc)



d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}
print("intial ",d)

p = d.popitem()
print("poped item", p)
print("after popitem",d)

p = d.pop("pname")
print("poped ",p)
print("after pop",d)

print()



d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}

# print("get using d['pid']", d["pid1"])
print("using get function", d.get('pid1',-1))


d.update({'pid':101})
print("update 1", d)


d.update({'pid':101, 'price': 30000})
print("update many", d)


# for keys sorted
d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}.keys()

print("initial",d)
d2 = sorted(d)
print("assending", d2)
d2 = sorted(d,reverse=True)
print("dessending",d2)


# for value sorted
d = {"pid" :'1001', "pname" : "mobile1", "price" : '23000', "company" :"samsung"}.values()

print("initial",d)
d2 = sorted(d)
print("assending", d2)
d2 = sorted(d,reverse=True)
print("dessending",d2)

# for items sorted

d = {"pid" :1001, "pname" : "mobile1", "price" : 23000, "company" :"samsung"}.items()

print("initial",d)
d2 = sorted(d)
print("assending", d2)
d2 = sorted(d,reverse=True)
print("dessending",d2)