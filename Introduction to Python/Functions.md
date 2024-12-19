
# Functional programming language:

```python
def Functiono_Name():
    pass
```

what is function?
- function is a set of statements
- a function is a piece of code or block of unit. 
- the main objective of function is to perform code reusability
    - which means once write and call any number of times.

## Types of functions
### predefined function
- predefined function can be represented as a function which is created or developed at the time of developing the programming language then it is said to be predefined function 
- ex:     print()
         id()
         zip()
         type()
         eval()
### user defined function
- user defiend function( custom function ) can be represent as a function which is created by programmer of developer at the time of writing the business logic then it is said to be user defined function
- in python user defined function can be created as def followed by function name
```python
def functionName():
    pass
```

---
what is __name__=="__main__":

it is a method is used to execute the piece of code or block of unit directly or indirectly as per the application requirement.

```python
def functionName():
    pass

if __name__=="__main__":
    functionName()
```

---
### code reusablity
once write call any number of times 

```python
def functionName():
    print("Fuction call")

if __name__=="__main__":
    functionName()
    print()
    functionName()
    print()
    functionName()
    print()
```


---
## formal parameters and actual parameters:

- formal parameters can be represented as if we are using one or more than one variable as parameter at the time of creating a function then it is said to be formal parameters.
- actual parameters can be represented as if we are using one or more than one value at the time of calling a function 



```python
def add(a,b): # formal parameter
    print(f"{a} + {b} = {a+b}")

if __name__ == "__main__":
    add(10,20) # actual parameter
```


write a python script display 5 product information reading all product values from the keyboard by calling function once.

---
### working on return keyword
return is a keyword in python. the main objective of return keyword a function can return another function as per the application requirement if you are using retun keyword inside a function the function must be called inside a function. other wise output will be `None`.


#### Assignment:
- write a python script display only None 

note: dont use print function and variables and diplay none

- write python script develop 7 meaningfull usecases using return keyword.

- write a python script develop scientific calulater using return keyword for every operation ask from the user



---
# types of arguments in functions:
- positional arguments 
- default arguments
- keyword arguments 
- variable length arguments 
- keyword variable length arguments

## positional arguments:
it is a combination of formal and actual parameters. positional arguments work based on the position what we have provided at the time of creating a function 

- write a python script use 5 formal and actual parameters and apply the positional arguments


## default arguments
default arguments can be represent as if we are using formal parameters with there values at the time of creating a function then it is said to be default argument. 
while working with default argument default argument must be placed in last place.


- write a python script develop 3 diffrent use cases by perfoeming an operation using default variable



### keyword arguments
keyword argument can be represent as if we are using actual parameters with there values then it is said to be keyword argument.


- write a python script display the employee details using default and keyword arguments


### variable length arguments
variable length arguments can be defined or declared as * followed by variable name. the main  objective of variable length argument is to read zero or more than one number of argument and perform the operations as per the application requrnment. variable length argument return the data in tuple format.

- write a python script expect addtion perform any operation and perform the total sum of all function using variable lenght argument


### keyword variable length arguments
keyword variable length arguments can be defined or declared or ** forllowed by variable name the main objective of keyword variable length argument is to represent the data in dictionary format(key : value pair format)


question 
- what is the diffrence between *variable_name and **variable_name?
    - *variable_name is variable length argument which represents the data in Tuple format.
    - **variable_name is keyword variable length argument which represents the data in dict format

example
- write a python keyword variable length argument and perform some operations on values using keyword variablel length argument


---
# types of variable
while working with functional programming language we do have following types of variable 
- global variable
- local variable
- how to define or declare global variable inside a function

## global variable
- global variable can be represent as a variable which is defined outside a function is called gloable variable 
- global  variable can be accessed anywhere in the program
```python
a = 10 # global varible
def function():
    pass
```

example
- write a python script read one string from keyboard as a gloable variable 
    - count and display the vowels
    - count and display the consonents
    - perform reverse of a string 
    - after performing reverse of a string check palindrome



## local variable

local variable can be represent as a varible which is defined or declared inside a function the it is said to be local varible. the scope of the local varible is within the function only.
```python
g = 293 # global varible
def function():
    l = 10 # local variable
```


## how to define or declare global variable inside a function

global varible can be defined or declared inside a function using global keyword followed by variale_name. the scope of global keyword varibale we can access any where inside program.

```python
def function():
    global g 
    g = 10

```

- write a python script develop meaningfull application logic using gloable, local varible and how to define and declare a global varible inside a function.



---
# lambda function 
working on name_less function / lamba function

- lamba function can be represent as a function which does not have any name then it is said to be lambda function.
- in python we can define or declare a lambda function using lambda keyword.

```python
square = lambda a: a*a
print(square(5))
```

- faster then def function
- take less lines

---
- filter()
- map()
- reduce()

## filter():
it is a predefined function in python. the main objective of filter() is to filter the data as per the application reqn. filter() function is applicable of name_full function and name_less/lambda function


- write a python script with name full and name less with filter function develop 7 diffrent meaning full use case.

## map():
it is a predefined function in python the main objective of map function is to take the each object from the list and perform some operation and store into another list
- map function is applicable for namefull function or nameless function(lambda)

- write a python script with namefull and nameless with map function develop 5 meaningful use cases

## reduce():
it is a predefined function in python the main objective of reduce function  is to combine the multiple objects into single entity.
- reduce function present in functool module.

```python
from functool import reduce
```
example
- convert to namefull
- write a python script with namefull and nameless with reduce function develop 3 meaningfull usecases.


---
# closures / Nested function / innerFunction :

Python supports nested functions or inner function. nested function or inner function can be represent as a defining or declaring a function inside another function then it is said to be nested function or inner function.

```python
def Function1():
    print("Function1")

    def Function2():
        print("Function2")
    Function2()
Function1()
```

write a python script develop 5 meaningfull usecases using nested or inner function

