#### 28-10-2024
# **Python Programming Language**

- [code](https://github.com/Anvesh1909/Python-Full-Stack/tree/main/Introduction%20to%20Python)

Python is a powerful, versatile programming language created by **Guido van Rossum**. It is widely used for various applications, from web development to data science.

## Creating a Virtual Environment
- A virtual environment is a workspace isolated for a specific project.
- It helps manage dependencies and avoid conflicts across projects by providing a dedicated area for project-specific packages and configurations.

---

## Functions in Python
Functions are a way to organize code into reusable blocks. They come in two types:

1. **Predefined Functions**: Built-in functions provided by Python.
2. **User-Defined Functions**: Functions created by the user to perform specific tasks.

**Example of a Predefined Function: `print()`**
- The `print()` function is used to display messages or values in the console.
- It can output strings (enclosed in `' '`, `" "`, `''' '''`, or `""" """`) or variable values.

**Example**:
```python
print("Hello, World!")
```

---

## Executing a Python File
To run a Python file on Windows, navigate to the file location in Command Prompt and use one of the following commands:

1. `Python filename.py`
2. `python filename.py`
3. `py filename.py`

Each command will execute the specified Python file (`filename.py`).

---
#### 29-10-2024
### **Difference Between a Program and a Script**

- **Program**: A Python application that does not rely on external modules and uses only built-in functions to accomplish its tasks.
  
- **Script**: A Python application that includes one or more modules (predefined or custom) to perform specific functions.

#### **Python as a Program**
If developers are writing business logic using only built-in functions without importing any modules, then it is considered a Python program.

#### **Python as a Script**
If developers are using one or more predefined modules in their code, then it is considered a Python script.

**Python has over 160,000 predefined modules.**

**Example - Using the `time` Module**
The `time` module allows for operations related to time, such as hours, minutes, and seconds. To use the `time` module, write `import time`.

```python
import time
time.sleep(3)  # pauses execution for 3 seconds
print("This is a Python script.")
```

- **Program Example**: [Program Code](./ProgramLanguage.py)
- **Script Example**: [Script Code](./ScriptingLanguage.py)

---
#### 30-10-2024
### **Difference Between Java and Python Programming Languages**

#### **Java:**
1. Java is statically typed.
   - Data types must be defined explicitly.
   - Example: `int a = 120;`

#### **Python:**
1. Python is dynamically typed.
   - Data types are determined at runtime, no explicit declaration is needed.
   - Example:
     ```python
     a = 30
     print(type(a))  # Output: <class 'int'>
     ```

---

# **Identifiers and Variables in Python**

Identifiers, also known as variables, are names given to values in Python code.

## **Rules for Writing Identifiers:**
1. Use characters from A-Z, a-z, 0-9, and the underscore (`_`) character.
   - Only `_` is allowed as a special character in identifiers.
2. Identifiers cannot start with a number.
3. No length limit for identifiers, though overly long names reduce readability.
4. Python identifiers are **case-sensitive**.
   - Example of case sensitivity:
     ```python
     A = 1500  # id(A) -> 10341
     a = 1233  # id(a) -> 22002
     ```
5. Identifiers should not use reserved keywords.
   - Python has 35 reserved keywords, including `True`, `False`, and `None` (title case), with others in lowercase.
```
'False', 'None', 'True', 'and', 'as', 'assert',
'async', 'await', 'break', 'class', 'continue', 'def',
'del', 'elif', 'else', 'except', 'finally', 'for',
'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield'
```

**Example of Valid and Invalid Identifiers:**
```python
# Valid identifier
_variable = 123

# Invalid identifiers
_ _ = 12
$ = 123
12Ab = 233
```

To display all Python keywords:
```python
import keyword
print(keyword.kwlist)
```

- **Code**: [Identifier Code](./identifier.py)

---

# **Software Development Life Cycle (SDLC)**
1. **Development Phase**: Writing and designing the code.
2. **Testing Phase**: Verifying that the code functions as expected.

---

# **Assignment 1: Identifiers**
1. **Task 1**: Write 15 examples of valid Python identifiers using the above rules.
2. **Task 2**: Write 15 examples of invalid Python identifiers.

- **code :** [Assignment 1](./Assignments/Assignment1.py)

---

# input function
it is a predefined function in python. the main objective of input() is to read the data dynammically values from keyword. while reading any data / information by default string will be returd

- [code to input](./Input.py)


---

# **Data Types in Python**

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

- [Datatypes](./DataTypes.md)
---

# Type Casting in python:
converting one data type into another data type using following function
- `int()`
- `float()`
- `bool()`
- `complex()`
- `str()`


# eval()
- the main objective function is to read anydata from the keyboard
- while reading string data type we must use '' or "" 
- eval function is also used to perfrom following operation
- NAO
- string concatination SC
- SR
- applying + between 2 strings is string concatination
- applying * between 2 strings is string repatation.


---

# Operators in python
[operators in python](./Operators/Operators.md)