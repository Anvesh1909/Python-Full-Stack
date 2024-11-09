# What is an operator?

An operator is a symbol which is used to perform operations between the operands 

in python programming language we do have following operators which are follows

- Arthimetic operators
- Assignment operators
- Logical operators
- Equality operators
- Comparision operators
- Ternary operators
- Chaining operators
- Special type of operators
- Bitwise operators

---
# Arthmatic operators
the main objective of arthmetic operators is to perform mathmatical operations as per the application requirement. following are the arthametic operations in python
` +, -, *, /, //, % `
- [Arthimetic operators](./ArthmaticOperators.py)
---
# Assignment operators
the main objective of Assignment operators is to perform the arithemetic operations by utilizing the memory management.
`=, +=, -=, /=, //=, *=, **=, %=`
- [Assignment operators](./AssignmentOperators.py)

write a python script to know the diffrence between arthemetic operator and assignment operators

---
# Logical operators
the main objective of Logical operators is to perform logical operation as per the application requiremt. following are the logical operators in python which are as follow:
- Logical and `and`.
- logical or `or`.
- logical not `not`.


### Truth Table for AND and OR Operations

| a | b | a AND b | a OR b |
|---|---|---------|--------|
| 1 | 1 |    1    |    1   |
| 1 | 0 |    0    |    1   |
| 0 | 1 |    0    |    1   |
| 0 | 0 |    0    |    0   |

### Truth Table for NOT Operation

| a | NOT a |
|---|-------|
| 1 |   0   |
| 0 |   1   |


### logical and 
returns true if both are true else false
### logical or 
returns true if any one of them is true else false
### logical not
return true if false else true 

---
# Equality operators

python supports equality operators. the main objective of equality operators is means comparision and return the boolean value either True / False. Following are the equality operators in python.
- `==`
- `!=`
 
---
# comparision operators
the main objective of the comparision operator to return the boolean values after checking the condition. following are the operators which are as follow:
` < , <= , > , >= `
- [comparision operators code](./comparisionOperators.py)

---
# chaining operators:
the main objective of chaining operators is to complex comparisions as the application requirement. while working with chaining operators condition if false then complete expression then result is false. chaining operators return boolean values

```
a = 100
b = 200
c = 300
d = 400
print(a,b,c,d)
print("result")
print(a<b<c<d)
print(a>b<c<d)
```

Write a python script to develop a meaning full usecase with chaining operator

---


# Ternary Operator:
- uniary operator 
- binary operator
- ternary operator

### uniary operator 
uniary operator can be represented as if we are using one operator with one variable or operand then it is said to be uniary operator

### Binary operator 
binary operator can be represented if we are using one operator with two variables or operands then it is said to be binary operator

### ternary operator
ternary operator can be represented as if we are using one or more than one variable with one or more condition then it is said to be ternary operator

```
a = 1000
b = 990
Max_Value = a if a>b else b # ternary operator
```

write a python script read 5 integer values from keyword display max and min object using ternary operator 

---

# special type of operators(STO) in python 

- Identity operators
- membership operators

### Identity operator

the main objective of identity operator is meant for **address comparision**. identity operators returns the boolean values after checking the condition
- `is` operator
- `is not` operator 

```
l1 = [1,2,3,4]
l2 = [1,2,3,4]

if any ojects are mutable then addresses will be diffrent is values are also
if it is immutable and have same values then its addresses are same

```

what is the diffrence between == and is operator?
`==` is a equality operator in python meant for content comparision
`is` is a identity operator in python meant for address comparision


write a python script develop one meaning full usecase using identity operator.

### membership operator 
python supports membership operators it is a special type of operator (STO) in python. the main objective of membership operator is to  search a charecter or group of character and return boolean values.
following are the membership operators in python
- `in`
- `not in`

write a python script