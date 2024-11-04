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


---

### **Tuple data type** :
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

