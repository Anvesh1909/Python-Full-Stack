# Object Relational Model(ORM)
- the main objective of django ORM is to perform the database task 
- ORM quary to fetch complete records
```python
from ORM.models import Employee

# select * from Employee;
obj = Employee.objects.all()
obj

<QuerySet [<Employee: 
            ID : 1 , Name : Anvesh , MobileNo : 1234 , Email : anvesh@gmail.com
        >, <Employee: 
            ID : 2 , Name : SATISH , MobileNo : 4321 , Email : satish@gmail.com
        >, <Employee: 
            ID : 3 , Name : SURYA , MobileNo : 3421 , Email : SURYA@GMAIL.COM
        >, <Employee:
            ID : 4 , Name : AJAY , MobileNo : 1243 , Email : AJAY@GMAIL.COM
        >, <Employee:
            ID : 5 , Name : UPENDER , MobileNo : 2134 , Email : UPENDER@GMAIL.COM
        >]>


# select * from Employees where name="Anvesh" limit 1
obj = Employee.objects.get(name="Anvesh
obj

<Employee:
            ID : 1 , Name : Anvesh , MobileNo : 1234 , Email : anvesh@gmail.com
        >


# insert into Employee("hello","hello","1234321","hello@gmail.com
obj = Employee.objects.create(name="hello",mobile="1234321",email="hello@gmail.com


```

<!-- - take a list with random numbers
- [1,3,4,45,55,6,7,7,2,8,45,55]
- print the repeated numbers -->
## insert data using  views.py
Employee.objects.create(name="jessica",mobile="123456543",email="jessica@gmail.com)




## All Objects
Employee.objects.all()

## one Objects
Employee.objects.get(id=1)


## filert Objects
Employee.objects.filter(name__startswith ="A")

## or
Employee.objects.filter(name__startswith ="A") | Employee.objects.filter(name__startswith ="s )


## update a record
a = Employee.objects.get(id=13)
a.mobile="98765436212"
a.save()

Employee.objects.filter(id=12).update(mobile="78955655665")

## delete
Employee.objects.get(id=11).delete()



## order by class
assessending order
Employee.objects.all().order_by("mobile")

decending order
Employee.objects.all().order_by("-mobile")

## limiting the quaries 
- in django ORM methodlogy LIMITING the queary is nothing but applying the slice operator 
Employee.objects.all()[0]
Employee.objects.all()[2]
Employee.objects.all()[2:]
Employee.objects.all()[2:5]
Employee.objects.all()[2:10:2]
Employee.objects.all()[::-1]


## Aggegate function 
- AVG, SUM, MAX, MIN, COUNT
- from django.db.models import Avg, Sum, Count, Max, Min
- Employee.objects.all().aggregate(Avg("id"))
- Employee.objects.all().aggregate(Sum("id"))
- Employee.objects.all().aggregate(Count("id"))
- Employee.objects.all().aggregate(Max("id"))
- Employee.objects.all().aggregate(Min("id"))

## delete all records
- Employee.objects.all().delete()

---
- develop a django application 
- develop the 25 plus orm quaryes for customer model
---
## sending the data from frontend to backend
- crispyforms
- it is a predefined module in django which internally uses bootstrap 
- `pip install django_crispy_forms`
- 