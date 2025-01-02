# Exception Handling
in programming language we do have two types of errors which are as follows
1. Syntax error
2. Runtime error(An Exception)


## Syntax Error
Syntax error can be represented as if we are not following the run of programming language then it is said to be syntax error 

## runtime error
runtime error is also known as exception. an exception can be represent as unwanted or unexcepted that disturb the follow of execution then it is said to  be run time error
- an excetionc can be occured via memory management or by end user

Note: An Exception is a class in python
---
### objective of exception
the main objective of the exception is to provide the graceful termination or normal even though wheather exception is handled

note: while working with an exception handling the root exception name is `BaseException`

- to overcome exception we use try and except:
- `try`: the main objective of try block is to put the risky code inside the block.
- `except`: the main objective of except block is to provide gracefull termination or normal termination

```python

try:
    # try block
except Exception as e:
    print(e)
    # except block

```
- we can use more than 1 except block with single try block to display the meaningfull message


### working with default except block:
default except block can be define or declare a if we are using except keyword without using exception__clas__name then it is said to be default except block
- while working with default except block. default expect block will placed at last.

- example: 
    - write a python script can we use more the one exception class with in single except block if possible write meaningful usecase

---

# finally block
finally is a keyword in python. the main objective of finally block is meant for resource deallocation(clean_up activity)
- finally block is executed whether the exception is handled or not handled 
- except one case if we use os._exit(0) which means pvm will be shutdown
- `os.exit(0)` ->  PVM will be shutdown
- `0` is status code 

Note: status code can be either positive number or negitive number including 0. 

---
# except else block
if except block will not be executed then else block will be executed 

- what is the diffrence between destructor and finally block
- destructor and finally are both meant for clean up activity or deallocation
- where destructor is meant for object level operations
- finally is meant for try  block operations

write the meaning full examples