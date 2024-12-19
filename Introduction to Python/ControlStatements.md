# control statement

the main objective of control statement is to control the applications by writing the logic as per the application reqn . i
- decision making statements
- itterative statements
- Transfer statement

# decision making statements
- if statements
- nested if statements
- if else statements
- if elif else statements

## if statement
- if is a dision making statement in python if 'if' condition is true then if block will be executed 

```python
if condition:
    # if block 
or 
if(condition):
    # if block
```

- write a python script develop diffrent 25 use cases using if statememt
- time = 5 mins 25 examples
- [code](./Control%20statements/25Examples.py)

## nested if statement
It is also known as inner if statement. nested if statement/ inner if statememt can be represent as defining or declaring if statement inside another if statement then it is said to ne nested if statement 

- note: while working with nested if statement or inner if statement if outer if statement condition is true then it will enter in inner if statement
```python
if condition1:
    # outer if
    if condition2:
        # inner if 
```

assignment
write a python script using nested if statement develop 5 meaningfull usecases

---

## if else:
if a else a decision making statement in python. if condition is satisfied then if block will be executed otherwise else block will be executed.
```python
if condition:
    # if block
else:
    # else block
```

1. user id , password using dict
2. to check a number is positive or negitive
3. even or odd
4. palindrome

assignment for if else statement
- write a python script develop 25 meaningfull usecases using if else statement

---
## if elif else:
the main objective of if elif else statement is to check more than one condition

```python
if condition1:
    # if block
elif condition2:
    # elif block 1
elif condition3:
    # elif block 2
.
.
.
else:
    # else block
```


Assignment
1. write a python script enter the marks of the student for 6 subjects from the keyboard find out the average after calculate the average or persantage provide the grade the system using if elif else statement.
2. write a python script enter the product details from the keyboard if the product price is more than 25000 apply 18% gst to that product. if the product price is less than 15000 apply 10% gst
if the product price is less than 5000 apply 5% gst using if elif else statement.
3. write a python script read 3 integer value from the keyword display the maximum object using if elif else statement. 
4. write a python script develop restaurent menu option using if elif else statement.



---

# Iterativve statement in python

The main objective of itterative statements is is to if you want to execute number of statements number of times then we can use iterative statements

following are the itterative statements in python
- for loop 
- nested for loop
- while loop 
- nested while loop

- Note: do while loop is not supported in python

## for loop
the main objective of for loop if you want to execute number of statements number of times if our data / information is in sequence 

```python
for i in range(10):
    # for block

for i in any_Sequence_datatype:
    # for block
```

### assignment
1. read one number from the keyboard display its table
2. find the nth largest element in list
3. find the largest and secound largest without using sort function


- read the number of vowels from the string 


1. write a python script read a number from the keyboard checkout whether a given number is palindrome or not 
2. write a python script generate a fibonocci serice using forloop 
3. write a python script read a number from the keyboard checkout the given number is armstrong number or not 
4. write a python script read a string from the keyboard checkout the given string is annagram or not ( listen -> silent )
5. write a python script develop 10 meaningfull example using for loop 


---
# Nested for loop

it is also known as inner for loop. nested for loops or inner forloop can be represented as defineg or declearing a for loop inside another forloop then it is said to be nested forloop or inner for loop

Note: while working with nested for loop or inner forloop if the outer forloop condition is true then inner for loop condition will be executed untill its condition is false.

```python
for (condition):   # outer forloop
    # outer for block
    for (condition):  # inner forloop
        # inner for block
```

001210122012
```python
for i in range(3):
    print(i)
    for j in range(3):
        print(j)
```


example:
```python



[A,B,C]
A
B
C
[D,E,F]
D
E
F
[G,H,I]
G
H
I




A
B
C
D
E
F
G
H
I



A B C D E F G H I



A B C
D E F
G H I
```

### assighnment

1. write a python script display 1:7 table all table must inn one row

2. write a python script perform matrix multiplcation using nested forloop.

3. write a python script perform transpose of the matrix usig nested forloop.

4. write a python script any 7 examples using nested for loop.



---

# zip function
it is predifined function in python. the main objective of zip function to perform the following operations
- it is used to convert from one data structure data type into another one 
- it is used to fetch more than 2 values 


---
# while loop 
the main objective of while loop if you want execute number of statements number of times if our data or information not in sequence or infite loop then we can go with while loop
the syntax for while loop is
```python
i = 0
while condition:
    # while block
or 
while(Condition):
    # while block
```
note : post increment oprator and pre increment operator is not supported in python (++,--)


1. write a python script read a string from the keyboard 
```python
0
1
2
4


A
B
C
D


A-0
B-1
C-2
D-3
```




# nested while loop ( inner while loop ):
it can be represent as defining and declaring a while loop inside another while loop then it is said to be inner while loop or nested while loop.
```python
while condition1:
    # outer while body
    while condtion2:
        # inner while body
```
note: while working with nested while loop/ inner while loop or inner while loop if the outer while loop contion is true then inner while loop is executed until its condition is false.



```python
l = [[1,2,3],[4,5,6],[7,8,9]]

output 1:
[1,2,3]
1
2
3
[4,5,6]
4
5
6
[7,8,9]
7
8
9



output 2:
1
2
3
4
5
6
7
8
9


output 3:
1 2 3 4 5 6 7 8 9


output 4:
1 2 3 
4 5 6
7 8 9

```



1. write  a python script read 2 list from the keyboard list data as follows 
['A','B','C']
[1,2,3]

```python
output 1:
A
1
2
3
B
1
2
3
C
1
2
3




Output 2

A--1
A--2
A--3

B--1
B--2
B--3

C--1
C--2
C--3
```


2. write a python script develop 7 meaning full usecases using nested while loop 



---
# Transfer statements in python:
- `break` statement 
- `continue` statement
- `pass` statement

### break
break is a transfer statement in python the main objective of break statemnet is to control the loops as and terminate the script as per the application requiremet.
break statement is always associated with itterative statement. either for loop or while loop 

#### for with else block
the main objective of for with else block if break statement inside the forloop is satisfied then else block will not be executed

```python
for i in iterable:
    if condition:
        break
else:
    # else block if braeak is not executed 
```


1. assume that my list is a group of numbers [1 to 10] if number 4 is there in the list display as the number is excits if number not found in list display that number is not there using for with else block



1. write a python script develop 10 meaningfull usecases using break statements
2. write a python script develop 5 meaningfull usecases using for with else block 

---

# continue statement
the main objective of continue statement is to skip the current itteraration if the condition is satisfied then continue for next iteration


1. write a python script write an even logic display odd numbers 
2. write a python script to know the exact diffrence of break and continue statements


---
# pass statement
pass is a transfer statement in python. pass means nothing or empty.

```python
def Functiono_Name():
    pass
```

Example:
1. write a python script develop 10 meaningfull usecases using pass keyword.
