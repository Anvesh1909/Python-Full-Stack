#### Date:- 2-11-24
### **Data Types in Python**
---

Python supports a wide range of data types for different kinds of data storage.

- **Integer**: Whole numbers, e.g., `10`
- **Float**: Decimal numbers, e.g., `10.5`
- **Boolean**: `True` or `False`
- **String**: Text, e.g., `"Hello"`
- **Complex**: Complex numbers, e.g., `3+4j`
- **List**: Ordered, mutable collection, e.g., `[1, 2, 3]`
- **Tuple**: Ordered, immutable collection, e.g., `(1, 2, 3)`
- **Set**: Unordered, unique collection, e.g., `{1, 2, 3}`
- **Dictionary**: Key-value pairs, e.g., `{"a": 1, "b": 2}`
- **Bytes**: Immutable binary data
- **Bytearray**: Mutable binary data
- **Frozenset**: Immutable set
- **Range**: Sequence of numbers
- **None**: Represents the absence of value

---
# Interger Data type
python support interger data type. it can be represented as 0-9. it may be either + number or - number of any size 
```
x = 123
print(type(x))
x1 = -12323
print(type(x1))
```

# Floating Data type 
python supports floating data type. it can be represented as decimal point number or floating point number. it may be + floating point number or - floating point number as `1.3d+e/E` also known as floating point number
- `f1 = 1.3e
           ^
SyntaxError: invalid decimal literal`

- `f1 = 1.3**10**10`
- e means 10 to the power n
- `1.3e2` 130.0 `1.3 x 10**2`
- `1.3e3` 1300.0
- `1.3e0` 1.3

# Boolean Data type 
python supports boolean data type. the main objective boolean data type is to return boolean values either True/ False after checking the condition.

# String data type
- String can be represented as collection of charecters or sequence of charecters enclosed with `' ' or " " or ''' ''' or """ """`.
- while working with string data type space is also considered as a charecter.
- python supports positive index which start from 0 to length-1. it is also known as forword direction
- python also supports negitive direction which starts from -1 to -length. it is also known as backword direction
- `''' ''' or """ """` also used for multiline content
- to create a string of 
```
I will be a 'software developer' after full stack python development
```
- string supports index and slicing


| Positive Direction | 0 | 1 | 2 | 3 | 4 | 5 |
|--------------------|---|---|---|---|---|---|
| Characters         | A | n | v | e | s | h |
| Negative Direction |-6 |-5 |-4 |-3 |-2 |-1 |


- index:
```
a = "Anvesh"

positive direction
  0   1   2   3   4   5
| --------------------- |
| A | n | v | e | s | h |
| --------------------- |
  -6  -5  -4 -3  -2  -1
negitive direction


name = "Anvesh"
print(name[0])
print(name[1])

print(name[-1])
print(name[-2])

output:
A
n
h
s
```
- slice operator: the main objective of slice operator is to make the pices of the string as per the application require.
- `s[ start : end : step ]`.
- while working with slice operator step cannot be zero
```
    print(name[::0])
          ~~~~^^^^^
ValueError: slice step cannot be zero
```


- [string code](./String.py)

---

# complex data type
the main objective of complex data type is to perform complex operations as per the application requirement
complex can be defined or declared as follows 
```
a = 100 +200j
b = -100 -200j
```

it is divided into 2 parts:
real - 100 - `a.real` --> 100.0
imaginary - 200j - `a.imag` --> 200.0



---
# List data type 
- if you want to represent one or more then one object or group of object in a single entity we can go with list data type
- in python we can define or declare list data type using `[] or list()`.

### properties of list data type
- insertion is preserved ( input data == output data )
- duplicate objects are allowed
- hetrogeneous objects are allowd 
- list is a mutable object ( state full object )
- list is dynamic or growable 
- indexing and slice operator is applicable 

while working with list data type in python we do have following prefefiend functions:

# functions in list:
- `append()`: it is used to add only one object at a time.
- `remove()`: it is used to remove only one object at a time.
- `extend()`: it is used to add more than one object or add complete a list from one list to another list
- `copy()`: it is used to copy the complete list object/ elements to one list to another list
- `insert(index, item)`: the main objective of insert function is to insert the data or information using indexing position either positive directive or negitive direction.
- `pop()`: it will remove the last objects in the list.
- `pop(index)`: Removes and returns the item at the specified index (default is the last item).
- `sort()`: Sorts the list in ascending order. it is only applicable for list data type.
- `sorted(list)`: Returns a sorted version of the list. can be used for any data type or information .
- `clear()`: Removes all elements from the list.



where can we use list data type in real world application?
in real world application list data type can be used to perform dynamic operations such as inserting the data, updating the data, deleting the data as per the application requirement.


---
# **Tuple data type** :
- python supports tuple data type. 
- if you want to represent more than one object or group of objects as a sigle entity then we can go with tuple data type. 
- in python we can define or declare tuple data type using `()` or `tuple()` function.
- while working with tuple data type `()` are optional.
 
#### properties of typle data type :
- insertion in preserved
- duplicate objects are allowed 
- hetrogeneous objects are allowed 
- tuple is a immutable object.
- tuple is not dynamic or not growable
- indexing and slice operator is applicable

---
### 1. Insertion is preserved
- input data == output data (ordered format is not changed)

### 2.duplicate objects are allowed 
- `(1,2,3,4,2,3,1)`

### 3. hetrogeneous objects are allowed
- `(1, 'Anvesh', 30.000)`

### 4. tuple is a immutable object(state_less object).
- state less object which means cannot change the values
- `t[1] = 19292` TypeError: 'tuple' object does not support item assignment

### 5. Tuple is not dynamic or not growable
- tuple is a not dynamic or nor growable because tuple is a immutable object.
- only `max() min() len()` are acceptable for tuple 
- `t.remove(1)` AttributeError: 'tuple' object has no attribute 'remove'

### 6. Indexing and slice operator is applicable for tuple 
- index start from 0 to length-1
- `t[0]`
- slice `t[ start : end : step ]`


#### *whare can use tuple data type in real world application.*
- in real world application tuple data type can be used to perform readability operations.
- tuple data type is more than list data type   

- [Tuple code](./Tuple.py) 

___
### 4-11-2024

# Set data type:
- python supports set data type. if you want to one or more than one objects or group of objects as a single entity then we can go with set data type. 
- in python programming language set data type can be define or declare `{}`

Note:
    in pyton programming language Set and Dict data type can be defined or declared as `{}`. 
    if we define or define or declare `{}` with empty then PVM will condider as dict data type

- to define an empty set use `s = set()`
- `{}` this defiens and empty dict

## properties for set data type:
- Insertion is not preserved
- Duplicate objects are not allowed
- Hectrogeneous objects are allowed
- set is a mutable object
- set is a dynamic and growable 
- index and slice operaters is not applicable

### 1. Insertion is not preserved:
- input data is not equal to output data 
```
enter the set data: {'a','b','c','d','e','f'}
a
c
f
d
e
b
```

### 2. Duplicate objects are not allowed:
```
enter the set data: {1,2,2,3,3,4,5}          
1
2
3
4
5
```

### 3. Hectrogeneous objects are allowed:
```
enter the set data: {1001, "Apple", 51000.21,'a'}
51000.21
1001
a
Apple
```

### 4. set is a mutable object (State full object):
```
before mutable operation
{'E', 'A', 'C', 'B', 'D'}
After mutable operation
Traceback (most recent call last):
  File "c:\Users\manve\Desktop\Python-Full-Stack\Introduction to Python\tempCodeRunnerFile.py", line 6, in <module>
    s1[1] = "z"
    ~~^^^
TypeError: 'set' object does not support item assignment
```

- Note: 
    set data type is a mutable object or state full object.
    updation or modification because of insertion is not preserved.

### 5. set is a dynamic and growable:
set data type is dynamic and growable which means we can increase and decrease the size of the set data type using following functions
- `add()` : it is used to add only one object at time.
- `remove()` : it is used to remove only one object at time.
```
s1 = set()

print("====initial set=====")
print(s1)

s1.add(1001)
s1.add("mobile")
s1.add(29000.50)

print("====after add opetaion====")
print(s1)

print("====after remove opetaion====")
s1.remove(1001)
print(s1)
```

### 6. index and slice operaters is not applicable:
```
Traceback (most recent call last):
  File "c:\Users\manve\Desktop\Python-Full-Stack\Introduction to Python\tempCodeRunnerFile.py", line 20, in <module>
    print(s1[1])
          ~~^^^
TypeError: 'set' object is not subscriptable
```
```
Traceback (most recent call last):
  File "c:\Users\manve\Desktop\Python-Full-Stack\Introduction to Python\tempCodeRunnerFile.py", line 22, in <module>
    print(s1[3:10])
          ~~^^^^^^
TypeError: 'set' object is not subscriptable
```

1. what is the diffrence between list and tuple data type?
2. what is the diffrence between list and set data type?
3. what is the diffrence between tuple and set data type?


- [set code](./Set.py)
---


## 1. Difference Between List and Tuple

| Feature              | List                        | Tuple                           |
|----------------------|-----------------------------|---------------------------------|
| **Mutability**       | Lists are mutable, meaning elements can be added, removed, or changed. | Tuples are immutable, so once created, their elements cannot be modified. |
| **Syntax**           | Defined using square brackets: `[1, 2, 3]` | Defined using parentheses: `(1, 2, 3)` |
| **Performance**      | Lists are generally slower than tuples due to their mutable nature. | Tuples are generally faster because they are immutable. |
| **Memory Usage**     | Uses more memory due to additional functionality for mutability. | Uses less memory, as immutability makes them more memory-efficient. |
| **Use Cases**        | Suitable when the data needs to be modified frequently. | Ideal for data that should not change throughout the program. |
| **Built-in Methods** | Lists have more methods, such as `.append()`, `.remove()`, `.sort()`, etc. | Tuples have fewer methods, mainly `.count()` and `.index()`. |
| **Hashable**         | Lists are not hashable, so they cannot be used as dictionary keys. | Tuples are hashable if they contain only hashable elements, allowing them to be used as dictionary keys. |

## 2. Difference Between List and Set

| Feature              | List                        | Set                             |
|----------------------|-----------------------------|---------------------------------|
| **Mutability**       | Lists are mutable and allow modification of elements. | Sets are mutable but only allow unique elements, and they are unordered. |
| **Syntax**           | Defined using square brackets: `[1, 2, 3]` | Defined using curly braces: `{1, 2, 3}` |
| **Order**            | Lists maintain the order of elements as they are added. | Sets are unordered collections, so elements have no specific order. |
| **Duplicates**       | Lists allow duplicate values. | Sets do not allow duplicate values; duplicates are automatically removed. |
| **Accessing Elements** | Elements can be accessed using indices, e.g., `list[0]`. | Sets do not support indexing or slicing due to lack of order. |
| **Use Cases**        | Suitable for ordered data where duplicates are allowed. | Useful for unique items and operations like unions, intersections, and set differences. |
| **Common Operations** | Supports operations like slicing, indexing, concatenation. | Supports set-specific operations like `.union()`, `.intersection()`, `.difference()`. |

## 3. Difference Between Tuple and Set

| Feature              | Tuple                        | Set                             |
|----------------------|------------------------------|---------------------------------|
| **Mutability**       | Tuples are immutable, so elements cannot be modified after creation. | Sets are mutable but only contain unique elements, and they are unordered. |
| **Syntax**           | Defined using parentheses: `(1, 2, 3)` | Defined using curly braces: `{1, 2, 3}` |
| **Order**            | Tuples maintain the order of elements as they are added. | Sets do not maintain any specific order of elements. |
| **Duplicates**       | Tuples allow duplicate values. | Sets do not allow duplicate values; duplicates are automatically removed. |
| **Accessing Elements** | Elements can be accessed using indices, e.g., `tuple[0]`. | Sets do not support indexing or slicing due to lack of order. |
| **Hashable**         | Tuples are hashable if they contain only hashable elements, so they can be used as dictionary keys. | Sets themselves are not hashable and cannot be used as dictionary keys. |
| **Use Cases**        | Ideal for ordered, immutable collections, especially for fixed data. | Suitable for unique, unordered collections, especially for set operations. |
| **Common Operations** | Limited operations such as `.count()` and `.index()`. | Set-specific operations like `.union()`, `.intersection()`, `.difference()`. |

---

# Dict data type:
- Python supports Dict data type. 
- if you want to represent one or more than one objects as key and value pair then we can go with dict data type.
- in python dict data type can be defined or declare using `{} or dict()`.
- in dictionary key should be unique

while working with dict data type we do have following predefiend funnction are as follow:

- keys()
- values()
- items()
- copy()
- clear()
- popitem()
- pop()
- get()
- update()
- sorted()

1. `keys()`:
it is used to fetch the keys as per the application requirement.
`d.keys()`
2. `values()`: 
it is used to fetch the values as per the application requirement.  
3. `items()`:
it is used to fetch the key and value pair as per the application requirement
4. `copy()`:
it is used to copy complete key and value pair from one dict to another dict need another dict to store
5. `clear()`:
it is used to clear the complect dict data/ information no need to take in another dict
6. `popitem()`:
it is used to remove or delete last key:value pair from the dict data type
7. `pop()`:
it is used to remove the particular value by passing key as a parameter 
8. `get()`:
it is useed to get the value by passing key as paramenter to the function
9. `update()`:
it is used to update the one or more than one key and value pair
10. `sorted()`:
it is used to sort the -keys -values or -keys and values also

what is the diffrence between list and dict data type?
what is the diffreance between dict and set data type?


## 1. Difference Between List and Dict

| Feature              | List                                 | Dict                                     |
|----------------------|--------------------------------------|------------------------------------------|
| **Structure**        | A collection of ordered, indexed elements. | A collection of key-value pairs where each key is unique. |
| **Syntax**           | Defined using square brackets: `[1, 2, 3]` | Defined using curly braces with key-value pairs: `{'key1': 'value1', 'key2': 'value2'}` |
| **Mutability**       | Mutable - elements can be added, removed, or modified. | Mutable - keys and values can be added, removed, or updated. |
| **Order**            | Maintains the order of elements as they are added (since Python 3.7). | Maintains the insertion order of key-value pairs (since Python 3.7). |
| **Accessing Elements** | Accessed by index, e.g., `list[0]`. | Accessed by key, e.g., `dict['key1']`. |
| **Duplicates**       | Allows duplicate elements. | Keys must be unique, but values can be duplicated. |
| **Use Cases**        | Useful for ordered collections of items where duplicates are allowed. | Ideal for collections of unique keys mapped to values, like a lookup table. |
| **Memory Usage**     | Generally uses less memory compared to a dictionary for the same number of elements. | Uses more memory due to key-value storage and hashing mechanism for keys. |
| **Common Operations** | Common operations include indexing, slicing, appending, sorting, etc. | Common operations include retrieving by key, updating values, and checking key existence. |

## 2. Difference Between Dict and Set

| Feature              | Dict                                 | Set                                      |
|----------------------|--------------------------------------|------------------------------------------|
| **Structure**        | A collection of key-value pairs where each key is unique. | A collection of unique elements without key-value pairs. |
| **Syntax**           | Defined using curly braces with key-value pairs: `{'key1': 'value1'}` | Defined using curly braces with single elements: `{1, 2, 3}` |
| **Mutability**       | Mutable - keys and values can be added, removed, or updated. | Mutable - elements can be added or removed, but only unique elements are allowed. |
| **Order**            | Maintains insertion order of key-value pairs (since Python 3.7). | Unordered collection, so elements have no specific order. |
| **Duplicates**       | Keys must be unique, but values can be duplicated. | Does not allow duplicate elements; duplicates are automatically removed. |
| **Accessing Elements** | Accessed by key, e.g., `dict['key1']`. | Does not support indexing or key-based access due to lack of order. |
| **Hashable**         | Keys must be hashable, while values can be any data type. | Elements must be hashable to ensure uniqueness. |
| **Use Cases**        | Useful for mapping unique keys to specific values, e.g., a lookup table. | Useful for collections of unique items and performing set operations like union, intersection, and difference. |
| **Set Operations**   | Does not directly support set operations. | Supports set operations like `.union()`, `.intersection()`, and `.difference()`. |


- [Dict code](./Dict.py)


---
# Bytes Data type:
- python supports bytes data type.
- the main objective of bytes data type is to work on audio/ video/ semi structure file(xml,json). 
- Byte should be range(0,256)
- byte data type is immutable object / stateless object.
```
res1[0] = 12
    ~~~~^^^
TypeError: 'bytes' object does not support item assignment
```
---
# ByteArray data type:
- python supports byte array data type 
- it is exactly same as byte data type.
- the only diffrence is bytes data type is a immutable object and byte array data type is a mutable object

what is the common diffrence between bytes data type and bytes array data type?

## 1. Difference Between Bytes and Bytearray

| Feature              | Bytes                                | Bytearray                                |
|----------------------|--------------------------------------|------------------------------------------|
| **Mutability**       | Immutable - once created, the data cannot be modified. | Mutable - the contents can be modified after creation. |
| **Syntax**           | Created using `b''` or `bytes()` function, e.g., `b'hello'`. | Created using `bytearray()` function, e.g., `bytearray(b'hello')`. |
| **Memory Efficiency**| More memory-efficient due to immutability. | Uses slightly more memory because of mutability support. |
| **Usage**            | Ideal for read-only data that represents binary data (e.g., files, network data). | Suitable for data that might need to be modified after creation (e.g., byte-level manipulation in networking). |
| **Methods**          | Supports methods like `.decode()`, `.hex()`, etc., for read-only operations. | Supports additional methods for modification like `.append()`, `.extend()`, `.insert()`, etc. |
| **Hashable**         | Hashable, so it can be used as dictionary keys or elements in sets. | Not hashable, so it cannot be used as dictionary keys or set elements. |
| **Performance**      | Faster in performance due to immutability. | Slightly slower in performance because of mutability support. |


- [Byte and Byte array code](./Byte.py) 
---

# Frozen set data type:
- it is exactly same as set data type
- the only diffrence is set is mutable object. but frozenset is immutable object

- [frozenset](./Frozenset.py)
---
what is the common diffrence between tuple data type and frozenset data type?



## 2. Difference Between Tuple and Frozenset

| Feature              | Tuple                               | Frozenset                               |
|----------------------|-------------------------------------|-----------------------------------------|
| **Mutability**       | Immutable - elements cannot be changed after creation. | Immutable - elements cannot be changed after creation. |
| **Syntax**           | Created using parentheses `()`, e.g., `(1, 2, 3)`. | Created using `frozenset()` function, e.g., `frozenset([1, 2, 3])`. |
| **Order**            | Maintains order, so elements can be accessed by index. | Unordered collection, so elements cannot be accessed by index. |
| **Duplicates**       | Allows duplicate values. | Does not allow duplicate values; duplicates are automatically removed. |
| **Accessing Elements** | Elements can be accessed using indices, e.g., `tuple[0]`. | Does not support indexing or slicing due to lack of order. |
| **Hashable**         | Hashable if it contains only hashable elements, so it can be used as dictionary keys. | Always hashable, so it can be used as dictionary keys or elements in other sets. |
| **Use Cases**        | Suitable for ordered, fixed collections of items. | Useful for immutable sets of unique items, especially when set operations are needed. |
| **Set Operations**   | Does not support set operations like union, intersection, or difference. | Supports set operations like `.union()`, `.intersection()`, `.difference()` with other sets. |

--- 
# range data type:

- the main objective of range data type is to generate the sequence of integer values. Range data type is associated with forloop.

```
for i in range(begin,end,step):
  
# starting from 0 to end-1:
for i in range(end):

```
- [range code](./Range.py)
---

to convet any chr to integer we use `ord('a')`

- ascci value of "A" starts from 65
- ascci value of "a" starts from 97

- [ascii code ](./ascii.py)

---
# Assignment 2
write a pyhton script develop 10 meaningfull usecases using range data type.

---

# None data type:
python supports none data type which means nothing or empty.

```
emp_sal = 20000.00
print("Empp_salary :",emp_sal)
print()
print("the data type is:", type(emp_sal))
print()

emp_sal = None
print("Empp_salary :",emp_sal)
print()
print("the data type is:", type(emp_sal))
print()

emp_sal = 50000.00
print("Empp_salary :",emp_sal)
print()
print("the data type is:", type(emp_sal))
print()
```
