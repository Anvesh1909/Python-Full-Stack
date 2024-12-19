

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

# Working on super keyword:
- super is a keyword in python.
- the main objective of super keyword is to access the parent members in child classes.
- the members can be methods or variables. 

= can we access all four methods from child class using super keyword : `yes`
= can we access all variables from child class using super keyword : `yes`

write a python script using super keyword develop 3 meaningfull usecases 
