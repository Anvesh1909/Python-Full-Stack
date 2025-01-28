# web scrapping with regular expression:

## regular expression:
python supports regular expression. it is also known as regex object. it can be represent as if you want to represent group of string as a pattern what you are searching then we can go with regular expression. in python if you want to implement regular expression with module named as re module

### real world applications:
- to write the business logic for client and server side
- to delelop pattern matching applications
- to develop interpreter/compiler/translator
- to develop digital curcuits
- to develop communication protocals like http,https,smtp,ftp


## functions in RE
- finditer()
- start()
- end()
- group()

### finditer()
- it is a predefined function in python. the main objecive of finduter() is to perform som operation as per application requiremnet
- `finditer("pattern","Targeted_pattern")

### start()
- it is a predefined function in python. the main objective of start() function is to return indexing position of our pattern where our pattern starts

### end() 
it return end+1

### group()
it returns targetted strings


---
## charecter classes 
- [ABC] -> A or B or C
- [A-Z] -> All uppercase A to Z
- [a-z] -> all lowercase a to z
- [0-9] -> only digits from 0 to 9
- [a-zA-Z] -> both uppercase and lowercase
- [a-zA-Z0-9] - both uppercase and lowecase with digits
- [^a-zA-Z0-9] - special charecters only


## predefined classes:
- \s -> only spaces
- \S -> Except spaces everything will be displayed
- \d -> only digits
- \D -> Except digits
- \w -> alphanumarical charecters with _
- \W -> except only alphanumarical charecters with _(special charecters)
- . -> it will display the complete pattern

---
## Quantifiers
while working with regular expressionwe do have following qunifiers which are as follow
- Here A means pattern we can use charecter class or predefined class instead of A
- A -> only 'A'
- A+ -> Minimum one A or more than one A's
- A* -> Minimum one A or more than one A with zero number of A's and end+1
- A? -> only one A at time and Zero number of A's with end+1
- A{3,5} -> minimum 3 A's and maximum 5 A's
  
- ^A -> wheather our pattern starts with A or not
- A$ -> whether our pattern ends with A or not 


---
while working with regular expressions we do have following predefined functions which are as follows 
- `match()`
- `fullmatch()`
- `serch()`
- `findall()`
- `sub()`
- `subn()`
- `split()`
---
- match function
  - match the pattern from the starting indexing position and order is importend
- fullmatch function
  - match the complete pattern and return that pattern 
- search function
  - serch and return that pattern. here sequesnce is matter if duplicate object found simple ignore them
- findall function
  - find the return that object inside the list data type 
- sub function
  - to replace the pattern with the another pattern 
  - `sub("\d","*",actual_string)`
- subn function
  - the number of times the replacement done
  - returns the data in tuple format
  - tuple contains 2 items
      1. changed string
      2. no of replacements
- split function
  - split the python string on particular string 
---
## Problem
1. write a python script develop one meaningfull usecase using sub and subn function 
2. write a python script using split function develop 3 meaning full usecases 
---

## RegEx object for mobile number:
- `[6-9][0-9]{9}`
- `[6-9]\d{9}`
- `[+][9][1][-][6-9][0-9]{9}`

or

- `[6-9]{1}[0-9]{9}`
- `[6-9]{1}\d{9}`
- `[+]{1}[9]{1}[1]{1}[-]{1}[6-9]{1}[0-9]{9}`

---
# problem
- write a python script create a regex object in such a way that 
  - `+91-9876543210`
  - `9876543210`
  - `91-9876543210`
  - `919876543210`
  
---
## regex object for gmail accout
- `\w[A-Za-z0-9]*@gmail[.]com`