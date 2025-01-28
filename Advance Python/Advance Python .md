
# Advance  Python ----> OOPL
when do we say a programming language is said to be object oriented programming language?
A. a programming language is said to be object oriented programming language is it contains classes, methods, objects and creating the objects for the class as per the application is said to be object oriented programming language
---
Note : while working with object oriented programming language the root class is Object_class.
---
### what is a class? 
class is a design or template or blueprint 

#### how to create a class in python. 
we can create a class in python using `class` keyword followed by class name.

```python
class ClassName:
    
```

### what is an object?
an object is a physical existence of a class or realtime entity
#### how to create a object in python 
`objName = ClassName()`
---

while working with object oriented programming language we do have following methods:
1. constructors
2. instance methods (Non static methods)
3. class methods
4. static methods

while working with object oriented programming language we do have following variables: 
1. insatnce variable
2. static variable 
3. local variable 
4. default variable 

---
# Methods
## 1. constructors
it is a method which can be defined or declared as follows 
```python
def __init__(self):
    pass
```
- the main objective of constructor method is to define or declare application variables
- constructor will be executed autometically when we create an  object of a class 
- per object constructor will be executed only once.
- if we donot define or declare constructor method expleicitly then PVM will define default constructor

- self is a parameter we can also use any variable name in that place 
    - self is highly reccomended 


## 2. instance methods (Non static methods)
can be defined or declared as followed 
`def methodName(self):`
- the main objective of instance method is to write the bussiness logic for application development
- we can assess instance method (non static method) using object reference variable 


## 3. Class Method
- class method can be defined or declared as follows 
`@classmethod` decorator which is as follows

```python
@classmethod
def methodname():
    pass
```
- the main objective of class method is to perfoem class level operations 
- we can assess class method using following ways
    - using object reference variable.
    - using class name.


## 4. static method 
we can define or declare a static method using `@staticmethod` decorator which as follows
```python
@staticmethod
def static():
    pass
```
- the main objective of static method is to perform general utilities or instance use
- we can assess static method using following ways
    - using object reference variable
    - using class name
---


### while working with object oriented programming language how can we read the data from the keyboard 
initialize data inside the construector 

- write a python script read the 4 employee information and display the 4 employee information by only creating 1 object

### while working with object oriented programming langauage we do have following variable which are as follows:
- instance variable ( Non static variable )
- Static variable 
- local variable 
- default variable 


# Instance variable ( Non static variable )
instance variable can be defined or declared using 
- self followed by variable name inside class and 
- outside the class using object referacnce variable

incstance variable can be defined or declared in following methods
- inside the constructor 
- inside the instance method ( Non static method )
- outside the class using object reference variable 



## __dict__:

it is a method which is used to display the information in key and value format.
---
operations can be performed for a variable
- defining or declareing 
- accessing or printing
- deleting 
- updating 


- deleting an instance variable using del keyword using del keyword


Note : - instance variable cannot be defined or declared inside the classmehtod / static method 
        - constuructor method is meant for declaration part where as
        - instance method is meant for to write business logic 


---

# static variable 
Static variable can be defined or declared 
- inside the class and outside the method
    - directly variable
- inside the method using 
    - classname followed by variable name
- outside the class using 
    - classname followed by variable name
- inside the classmethod 
    - using classname or cls followed by variable name

- we can assess the static variable using class name not the object reference varible 



---

write a python script perform following operation for static variable
- defining or declaring 
- printing or accessing 
- deleting 
- updating


---

# local variable 
we can define or declare a local variable inside the constructor, instance method, class method, static method the scope of the local variable we can assess with in the methods not outside the method.

example: write a python script define or declare instance variable, static variable and local variable develop one meaningfull usecase 


---
# default variable 
self is a default variable the main objective of default variable define or declare instance variable inside the constructor and access them inside the instance method.

---
# inner classes / nested classes
python supports innerclasses or nested classess. it can be represent as defineing or declaring a class inside another class then it is said to be inner classes or nested classes

without existing one object there is no chance of existing another of object then we go with inner classes / nested classes.

```python
class Car_Class:
    class Engine_Class:
        pass


class Univercity_Class:
    class Collage_Class:
        pass
```

- write a python script develop 2 meaning full usecases using inner class.

---

# working on GC module

it is a predefined module in python which is by default enabled 

- gc stands for garbage collector
- the main objective of garbage collector is to distory the useless objects.

### what is usefull object ?
an object which is pointing to the class and its properties then it is said to be usefull objects

```python
S1 = Students()  # usefull objects
```

### what is useless object?
an object which is not pointing to the class and its properties then it is said to be useless objects

```python
S1 = Student()  # usefull object
S1 = None # useless object
del S1 # useless object
```

# distractor 
it is a method in python which can be defined or declare distructor method as follows

```python
def __del__(self):
    pass
```

the main objective of distructor method is to clean the memory blocks or resource realocation 


- what is the diffrence between del and None keyword while working with garbage collector keyword

`del`: used to delete the reference variable 
`None`: is used to change the address to None 

- write a python script what you understood in garbage collector develop 3 meaning full usecases

---

# Composition and aggregation 
Composition:
- composition is also known as strong relationship 
- it can be represent the relationship between an instance variable and object is called composition(Strong Relationship)
aggregation:
- Aggregarion is known as weak relationship. 
- it can be represent as the relationship between a static variable and object is called aggregation

---