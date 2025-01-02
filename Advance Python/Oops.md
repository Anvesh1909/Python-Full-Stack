

# inheritence in python
it is the process or methodology to extend from one class to another class.
- the main objective of inheritence is to provide the code reusability
- in python we have the following types of inheritence
    - single inheritence
    - multi level inheritence 
    - hirarchical inheritence
    - multiple inheritence 
    - hybrid inheritence

## single inheritence
it is the process or methodology to extend from one parent class to only one child class then it is said to be single inheritence.
```python
class Univercity:
    pass

class Collage(Univercity):
    pass
```
## multilevel inheritence
it is the process or methodology to extend from one class to another class continously then it is said to be MuiltiLevel inheritence

```python
class A:
    pass
class B(A):
    pass
class C(B):
    pass
```

## hirarchical inheritence
it is the process or methodology to extend from one parent class with model then one child class then it is said to be hirarchical inheritence.
```python
class Parent:
    pass
class Child1(Parent):
    pass
class Child2(Parent):
    pass
```

## multiple inheritence 
it is the process or methodlogy to extend more then one parent class with single child class then it is said to be multilevel inheritence
```python
class A:
    pass
class B:
    pass
class C(A,B):
    pass
```
note: while working with Multiple inheritence if the methods are same in python multiple inheritence can be implemented using a MRO(Method resololution order) algorithm

MRO RULES:
- rule 1: 
    - first it will serch in child class 
    - it there is no implementation it will start searching based on order what we have provided in our python script
- rule 2:
    - it follows left to right methodlogy 

## hybrid inheritence 
it is a combination of single, multilevel, hirachial, multiple inheritences.



mro():
it is a predefined function in python the main objective of mro() is to display the mro of the class

- develop the algorithm as per your diagram and write the code for then 2 examples
 
---

## Working on super keyword:
- super is a keyword in python.
- the main objective of super keyword is to access the parent members in child classes.
- the members can be methods or variables. 

= can we access all four methods from child class using super keyword : `yes`
= can we access all variables from child class using super keyword : `yes`

write a python script using super keyword develop 3 meaningfull usecases 


---

# Polimorphism
- Poly means - many
- Morph means - forms
- in python polymorphism can be implemented using following methodologies
    - overloading
        - operator overloading
        - method overloading
        - constructor overloading
    - overiding
        - method overloading
        - constructor overloading   
    - Duck Typing


=>  + can be used for addition or string concatination
=>  * can be used for product or string repeation 

## operator overloading
- python support an operator overloading using magic method.
- the following are the magic method in python 

+ Magic method for Arthemetic operator:
    - `+` -> def __add__(self,other):
    - `*` -> def __mul__(self,other):
    - `-` -> def __sub__(self,other):
    - `/` -> def __truediv__(self,other):
    - `//` -> def __floordiv__(self,other):
    - `**` -> def __pow__(self,other):
    - `%` -> def __mod__(self,other):



+ Magic method for Arthemetic operator:
    - `+=` -> def __iadd__(self,other):
    - `*=` -> def __imul__(self,other):
    - `-=` -> def __isub__(self,other):
    - `/=` -> def __itruediv__(self,other):
    - `//=` -> def __ifloordiv__(self,other):
    - `**=` -> def __ipow__(self,other):
    - `%=` -> def __imod__(self,other):
    - `>` -> def __gt__(self,other):
    - `<` -> def __lt__(self,other):
    - `>=` -> def __gte__(self,other):
    - `<=` -> def __lte__(self,other):
    - `==` -> def __mod__(self,other):
    - `!=` -> def __mod__(self,other):


- to return a str for an object the we can use __str__(self) method to print the object 
- write a python script using assignment magic method first perform addition the perform multiplication 
- write a python script using magic method develop 2 meaning full usecases 


---
# method Overloading
- method overloading can be represent as same method name with 0 or more than one number of arguments (diffrent number of arguments) then it is said to be method overloading.
- note : python doesnot support method overloading we can get feature using default argunment and variable length argument.

## method overloading with default argument:
- method overloading with default argument can be implemented if you want to read 3 or 2 number of arguments and perform the operations then we can go with method overloading with default argument.

## method overloading using variable lenght argument:
- method overloading uisng variable length argument can be represent as if we are reading 0 or n number of arguments and perform the operations then it is said to be method overloading using variable length argument.


## constructor overloading
-  constructor overloading can be represent as same constructor name with zero or more number of arguments then it is called constructor overloading

note : in python programming language constructor overloading is not supported we can achive this feature using default argument and variable length argument


---
# method overriding
python support method overriding & constructor overriding.
- example : write a python script as we know that python support method overriding & constructor overriding develop one meaning full usecase

---

# DUCK typing
it is the process or methodology to write same method name with its functionality then it is said to be duck typing methodology

example: write a python script develop one meaning full usecase for ducktyping to perform some operation.

---
# Encapsulation 
- python supports encapsulation. 
- it is the process or methodlogy to hide the internal implementation and showing the sevices then it is said be encapsulation .
- in python encapsulation can be implemented using following method.
    - `setter()` : it is used to set the data
    - `getter()` : it is used to get the data
- the main objective of encapsulation is to provide the secutity to the data/information 

example: write a python script develop one meaningfull usecase using encapsulation

---
# Abstraction
- Abstract method
- Abstract classes
- An interface 
- Concrete classes
- Access modifiers

## Abstract method
- Abstract method can be defined as we define or declare methods eventhough we dont know the implementation such methods are called abstract methods 
- Abstract methods are present in abc module 
- we can define or declare abstract methods using @abstractmethod decorator.

## Abstract classes
- we can define or declare using ABC attribute which is present in abc module.
- the main objective of abstract class is to provide partial implementation.

## An interface
- An interface can be represent as if abstract classes contain only contain abstract methods are called an interface.
- in real word application an interfact used for specification of the project.

- `globals()[]`: it is used to convert a string into object.

write a python script what you understood using interface devlop one meaningfull usecase

`q1)` what is the diffrence between abstract classes and interfaces?
- abstract classes can have abstract methods and non abstract methods as well
- an interfact can have only abstract methods 

---

## concrete classes

the main objective of concrete classes is to provide the complete services to the application 

- why do we require concrete classes

---
## Access Modifiers in python
python supports following types of access modifier which are as follows
- public 
- protucted 
- private

### public
public is a access modifier in python. we can define or declare as follows.
```python
A = 1000
```

the scope of the public access modifier we can access anywhere in our entire application

### protected 
protected is a access modifier. we can define or declare using _ followed by variable name 
```python
_b = 2000
```

the scope of protected modifier we can access with in the class and outside the class as well.

### private
we can define or declare using __ followed by variable name 
```python
__c = 3000
```
the scope of the access modifier we can access within the class but not outside the class.

ERP application functional domains as follows
ERP apps - banking, healthcare sector application, telecommunication application, aeroplane control system application
example : 
1. write a python script can we apply access modifiers to method if yes develop a meaningfull usecase  
2. write a python script can we apply access modifiers to the class to the classes if yes develop one meaningfull usecase
3. write a python script develop complete end to end operations of banking application
---


