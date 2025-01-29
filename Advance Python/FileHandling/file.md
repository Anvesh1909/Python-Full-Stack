# File handling in python 
- is to store the limited data and perform the operations as per the application requirement
- while working with file handling we do have following we do have following funtions and attributes as follow
    - `open()`: it is used to open the file
    - `close()`: it is used to close the file
    - `name` : it is an attribute which is used to know the file name
    - `mode`: it is an attribute which is used to know the mode of the file
    - `closed`: it is an attribute which is used to know whether the file is closed or not
    - `readable()`: it is used to know whether a file is readable or not
    - `writeable()`: it is used to know whether a file is writeable or not
---
## type of data can be stored
- alphanumeric data
- binary data
---
to store alphanumeric data we do have following mode
- `r` -> only read mode
- `r+` -> read and write mode
- `w` -> write mode
- `w+`-> write and read mode
- `a`-> append mode
- `a+`-> append mode read mode
- `x`-> exclusive mode
- `x+`-> exclusive and read mode
--- 
to store binary data
- `rb` -> only read mode
- `r+b` -> read and write mode
- `wb` -> write mode
- `w+b`-> write and read mode
- `ab`-> append mode
- `a+b`-> append mode read mode
- `xb`-> exclusive mode
- `x+b`-> exclusive and read mode
---
note: while working with filehandling by default read mode will be selected 

---

# write functions in file handling
- write()
  - it is predefined functions in python it is used to 
- writelines()
  - it is predefined function in python the main objective of write lines function to store their properties.

---
# Problem:
write a python script store 10 product information by using writelines function should be used only once

---
# read
- to read the data from the file to console or application console we do have following predefine functions which are as follows
- read() : complete content
- read(n) : no of charecters
- readline() : only one line from the file
- readlines() : conplete data and returens the data in the form of list 
---

- n is the number of charecter and \n is considered as 1 



---
## tell and seek function
- `tell()`:
  - the main objective of tell function is to know the currunt file pointer position
  - by default current file pointer position is `0`.
- `seek()`:
  - the main objective of seek function is to change the position of the file pointer.


---
# interview question
- what is the diffresnce between tell and seek function explain with an example?

---

## creating a file using with statement 
- the main objective of using with statement file will be closed automatically 
- following is the syntax for with statement
  - `with open("file_name","mode") as f:`


---
# pickling(packing) and unpicking(unpacking)
## pickling:
- it is the process or methodology to store the object information into a file in binary format.
- to implement pickling in python we have a module named as pickle module inside the pickle module we do have a dump  


---
# CSV module
- the main objective of csv module is to work in csv file 
- to implement csv we do have csv module.
- `writer()` -> used to write the csv file
- `reader()` -> it is used to read the csv file
- `writerow()` -> it is used to create the csv file with its name
---
- develop one meaningfull application logic using picking and unpicking along with csv module.


---
# Ziping and unzipping
- it is the process or methodlogy to convert one or more than one files into a zip folder format. 
- the main objective zipping method to decrease the sizze of the file.
- to implement zipping in python we do have a module named zipfile  module 
- we do have a class named `ZipFile("File_Name","mode",ZIP_DEFLATED)`
- winrar software must be installed to execute ziping in python

## Unzipping
- it is the process or methodlogy to read the file name with its content 
- then it is said to be unzipping methodlogy
- module named zipfile inside that we do have a class name
-  `ZipFile("filename","mode",ZIP_STORED)`
- namelist(): it is used to list all the file names inside the zip file



---
# objects serialization and deserialization
- it is a process or methodlogy to convert the python object into javascript json object
- then it is said to be object serialization 
- to implement object serialization we do have a module named as `json` module
- inside the json module we do have nested module called `dump(object,filename)` 

| Python Object      | JavaScript Object |
|--------------------|-------------------|
| Int, Float         | number            |
| String             | string            |
| True/False         | true/false        |
| None               | null              |
| List, Tuple, set   | An array          |
| Dict               | An object         |

## deserialization
- it is the process or methodology to convert json object into python object
- in read mode using function `json.load(f)`
---
Questions
1. what is the diffrence between zip function and zipping methodlogy in python explain with an example
2. 
