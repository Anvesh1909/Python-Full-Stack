# Packages in python 
- what is a module 
- what is package
- what is library 
- what is Framework

---
### what is a mobule
A module can be represent as if it contains classes, methods, functions, variable then it is said to be a module.
our python program or script is a module 
example : 
```python
demo.py
```
---
### what is package
a package can be represented as collection of one or more than one module then it is said to be a package
example:
```
package_1
    demo1.py
    demo2.py
    demo3.py
```
---
### what is Library
a library can be represented as one or more than one package then it is said to be a library 
example:
```
Library:
    package_1:
        demo1.py
        demo2.py
    package_1:
        Test1.py
        Test2.py
```
---
### what is a framework
framework can be represent as collection of one or more than one library then it is said to be framework 
```
Framework:
    Library1:
        package_1:
            demo1.py
            demo2.py
        package_1:
            Test1.py
            Test2.py
    Library2:
        package_1:
            demo1.py
            demo2.py
        package_1:
            Test1.py
            Test2.py
```

---
## Packages
- packages can be represent as one or more than one module then it is said to be package in python 
- in python if we use `__init__.py` which indicates that it is a package in python 
    - `__init__.py` is a empty file which indicates that it is a python package

- package is nothing but a folder or directory 
- as per the application requirement we may use nested packages.


develoop a package for employee management system our modules are inside the employee manageent system 
- register module
- login module
- department module 
- hr module


---
## Moduler Programming language
the main objective of moduler programming lalnaguage is to import and export the data/information from one module to another module or one application to another application 

it we import the module name more than one time that module will display only one time because data information will be stored in harddisk area 

---
## working with math module
the main objective of math module is to perform complex mathametical operations.
```python
import math
print(dir(math))
```
---
## Working with random module
the main objective of random module is to generate the random objects. random module is widely used in gaming application development 

```python
from random import *
print("===sub-Modules====")
print(dir(random))
```

while working with random module we do have following predefined functions which are as follows 
- `random()`: it generate the random values from 0.0 to 1.1 upto 15 decimal points
```python
from random import *
print(random())
``` 
- `randint()`: it generate the random objects or random otp's and mobile numbers as well.
```python
from random import *
print(randint(10000,99999))
```
write a python script generate 1000 random mobile numbers . mobile number should must be 10 digits and first mobile number start from either 6,7,8,9
- `randrange(begin,end,step)`: to generate the random object as per the application requirement
```python
from random import *
print(randrange(10))
print(randrange(200,1000))
print(randrange(200,800,2))
```
write a python script to know the exact diffrence between randint and randrange function develop one meaningfull usecase

- `uniform()`: to generate random floating point objects as per the application requirement
```python
from random import *
print(uniform(10,20))
```

- `choice()`: to generate random string objects.
```python
from random import *
l = ['A','B','C','D','E','F','G','I']
for i in range(10):
    print(choice(l))
```

write python script to generate the random objects for alphanumeric charecter (Upper,lower,special) develope one meaning full usecase 

---
# Numpy (Numeric Python)
the main objective of numpy is to work on data science applications. Numpy represents the data in array dimentions format. the dimention can be 0 to nth dimention.
numpy means numerical python.
- to install numpy . `pip install numpy`

- write a python script for 2 dimentional data apply slicing with positive and negitive direction 

### Shape 
it is an attibute in numpy module. it will give the dimentions and object from an given array  ( r X c )


### reshape()
it is a predefined function in numpy module it returns the data in 2 dimentional format 
the main objective of reshape function is to convert the one dimention into more than one dimention as per the application requirement



1. idea on linear equation
2. idea on algebra
3. idea on integration
4. idea on laplas transform 


- write a python script develop one meaningfull usecase what you understood using numpy module 






- develop one meaning full application to know the exact diffrence between math and numpy module 


---
# Pandas 

it is predefined module or library the main objective of pandas library is to work on data science applications . pandas represents the data in tabular or rows and coloum format using data frames `DataFrame()`  objects.

- install pandas `pip install pandas`



### head()
it is a predefined function in pandas module . The main objective is to know top n rows 

### tail()
it is a predefined function in pandas module . the main objective is to know the bottom rows

- write a python script how can we find middle rows of the pandas table


### sum()
it is used to perform coloum wise sum


### sum(1)
it performs row wise sum only integer or float values

### max()
it is used to display the max value coloum wise

### min()
it is used to display the min value coloum wise 

### count()
it is used to count the pandas objects using coloum wise 

---
## for iterator
- iteritems()
- iterrows()
- itertuples()

### iteritems()
it is used to fetch the data colum wise

### iterrows()
it is used to fetch the data row wise

### itertuples()
it is used to fetch the data tuple format


---
# working with csv
```python
import csv
with open("Students.csv","w",newline="") ad f:
    res1 = csv.writer(f)
    res1.writerow(["id","name","age"])
    n = int(input("Enter the number of rows"))
    for i in range(n):
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        res1.writerow([id,name,age])

```


---


