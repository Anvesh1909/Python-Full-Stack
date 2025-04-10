# 1
def details(name,age):
    return f"my name is {name} and my age is {age}"

print(details("Anvesh",'22'))


# 2
def func1(*args):
    print("printing values")
    for i in args:
        print(i)

func1(20,40,60)
func1(80,100)



# 3
def calculation(a,b):
    return a+b,a-b

res = calculation(40,10)
print(res)


# 4
def show_employee(name,salary=9000):
    print(f"Name: {name} salary: {salary}")

show_employee("Ben", 12000)
show_employee("Jessa")


# 5
def outer(a,b):
    def inner(a,b):
        return a+b
    return inner(a,b)+5

print(outer(10,20))


# 6
n = 10

def reccurAdd(a):
    if a == 1:
        return 1
    return a + reccurAdd(a-1) 

print(reccurAdd(n))



# 7
def display_student(name, age):  
       print(name, age)  

display_student("Emma", 26)

show_tudent = display_student
show_tudent("Emma", 26)



# 8
res = [ i for i in range(4,30) if i>=4 and i<=30 and i%2==0]
print(res)


# 9 
x = [4, 6, 8, 24, 12, 2] 
m = 0 
for i in x:
    if m<i:
        m = i
print(m)


