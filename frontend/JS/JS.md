# Why JavaScript
- 9ohniov snuo;bv uoi;abwnUO;CBINSAIUB VUI;BVNL;VIUBouhn buodhnvusob;vntsruo;nhfus;ounh bso;uuuuuuunlao;
-
- it can be written in 3 diffrent ways
- javascript is a client side scripting language
- the main objective of javascript is to develop interactive or dynamic web appliaction 
- javascript is a dynamically typed scripting language
    - no need to define the data type of a variable
- javascript is a interpreter scripting language
- javascript is a object based scripting language
- javascript allows object oriented programming language
- inside the javascript we can add the html and html5 tags
- html and html 5 tags are act as a object  

---
## ways to write the javascript
- we can write javascript code in 3 ways
1. inside the body tag using script tag
2. inside the head tag followed by script tag
3. external js using `.js` extention file
---
### where can we use javascript in realworld application
- to write the business logic for client_side validation
- to develop dynamic dropdown menu's
- to develop data and time live format
- to work on dialog boxes to perform dynamic operations
---
# `document.write():`
- it is a javascript method/function which is present in DOM. the main objective of this method is to display the dynamic message as per the application requirement
---
# write
```js
document.write("Hello World!");
```

---
## how to define or declare variables in javascript
- in js we can define or declare variables as follows
- var, let, const

---
## `console.log()`
- it is a javascript method/function. 
- it is used to perform debugging operations at client_side
---
## dialog boxes in javascript 
- it is used to provide the intemation to the end user 
- following dialog boxes supported in javascript
    - alert() or window.alert()
    - confirm() or window.confirm()
    - prompt() or window.prompt()
- note: on the webpage dialog boxces are the first entry point. 
- `alert()` : to provide the intimation to the end user with one dialog box
- `confirm()` : to provide the intination to end user with ok and cancel button
- `prompt()` : to read the data from the keyboard

---
# TypeCasting
- it is the process to convert one type of data into another type of data using following functions
    - `parseInt()`
    - `parseFloat()`
    - `Number()`
- example : 
    - write a javascript code if javascript supports eval function explain its functionality by writing the javascript code 
--- 
# data types in javascript 
- we can check the data type using `typeof()` 
- javascript supports following data types which are as follows 
- primitive data types
- non premitive data types
## primitive data types
- number data type : integer or float values with positive or negitive
- string data type : string is a group of charecters
- boolean data type : `true` or `false`
- null data type : typeof() will return object  `typeof(null)`
- undefined data type : initializing a variable but not declared the object is undefined
```javascript
let i = 10;
console.log(typeof(i))

let f = 3.14;
console.log(typeof(f))

let s = "Anvesh";
console.log(typeof(s))

let b1 = true;
let b2 = false;
console.log(typeof(b1),typeof(b2))

let n = null;
console.log(typeof(n))

let a;
console.log(typeof(a))
```
## non premitive data types
- An array data type
- an object data type
- regex object data type
## array
- in javascript an array data type can be defined or declare in following ways
- using an array literal 
- using an instance of an array 
- using an array construtor



---
- using an array literal 
```javascript
let ages = [21,22,23,24,25];
document.write("Ages are:",ages);
document.write("<br>data type is: ",typeof(ages));


document.write("<br>Using indexes:<br>");
document.write(ages[0]);
document.write(ages[1]);
document.write(ages[2]);
document.write(ages[3]);
document.write(ages[4]);
```
- using an instance of an array 
```javascript
let details = new Array();
details[0] = 1;
details[1] = "Anvesh";
details[2] = 25000;
details[3] = true;

document.write("details : ",details);
```
- using an array construtor
```javascript
let d = new Array(1,"Anvesh",25000.00,true);
document.write("details : ",d);
```


### array methods
- `push()`
    - it is a predefined function or method in javascript.
    - the main objective of push method is to add one or more than one object inside array
- `pop()`
    - it will remove the last element in the array
- write a javascript code using pop function remove the particular element from an array

---
## Object data type
- it is also know an JSON(java script object notation)
- can be defined or declared  in following ways
    - using object literal
    - using an instance of an object
    - using an object constructor
### using object literal
```javascript
let std_details = {
    "id" : 1,
    "name" : "Anvesh",
    "fee" : 290000.00,
    "present" : false
}
```
### using an instance of an object
```javascript
let std_details2 = new Object();
std_details2.id = 1;
std_details2.name = "ANvesh";
std_details2.fee = 290000.00;
std_details2.present = false;
```
### using an object constructor
```javascript
function std_details3(id,name){
    this.id = id;
    this.name = name;
}

std1 = new std_details3(1,"Anvesh");
std2 = new std_details3(2,"bunny");
```



---
# control statements
- Java script can be used as functional programming language as well
- we can create a function in javascript using function `keyword` followed by function_name.
- What is a function?
    - a function is block of code. 
    - the main objective of a function is code reuseability 
    - once write call any number of times
    ```javascript
    function function_name(){
        // function block
    }
    ```
---
Type of function in js
- using name_full function(using `function` keyword)
    ```javascript
    function test(){
        console.log("Welcome to functions in javascript");
    }
    ```
- using name_less function()
    ```javascript
    let hello = function(){
        console.log("hello world!");
    }
    hello()
    ```
- using arrow function(using arrow)
    ```javascript  
    let arrow = () => {
        console.log("HELLO ARROW FUNCTION")
    }

    arrow()
    ```

---
- ex :- write a javascript code develop one meaning full usecase of rest paraments
## rest parameters(variable length arguments)
- java script supports rest parametets 
- we can define or declare rest parameter ... followed by variable name 
- the main objective of rest parameter is to read zero or more than one number of arguments and perform the operation as per the application requirement 
---
# Control Statements in javascript
- if statement
- if else statement
- if else if statemnt

# itterative statements
- for loop 
- nested for loop
- while loop 
- nested while loop 
- do while loop
- for in loop
- foreach loop

# loop control statements
- break statement
- continue statement
- switch statement
---
## if statememt:
- decision making statemnt
- if block condition satisifiend then if block will be executed
```javascript
if(condition){
    // if block
}
```
- write a javascript code develop 7 meaningfull usecases using if statements
---
## For loop in javascript
- it is a control statement in javascript 
- if you want to execute the number of statements in number of times and if our data is in sequence 
- then we can go with forloop 
```javascript
for(start; end; step){
    
}

for(let i=startvalue; endCondition; step){

}
```
- write a javascript code develop 5 meaningful usecases using forloop
- write a javascript assume the my 2 arrays are
    A1 = [1001,1002,1003,1004] 
    A2 = ['A','B','C']
    1001 --- A
    1001 --- B
    1001 --- C
    1002 --- A
    .
    .
    .
    1004 --- C

- write a javascrript code display 10 to 100 table using nexted forloop in javascript code

---
## While loop
- if our data is not in sequence or infinte loop then we can use while loop 
```javascript
while(condition){

}
```
- write a javascript code assume that my array contains some list of prices perform the sum of the list using while loop 
- write a javascript code read a number from the keyboard and display table using while loop


---
## break statement
- stop the loop if the condition satisfies
## continue statement
- skip the current iteration if the condition satisfiend 
---
## javascript interview question
- what is the diffrence between break and continue statement write this with example with while and for loop
---
## Switch Statement:
- check more than one condition
```javascript
let a = window.prompt("Enter a charenct A-D: ")
switch(a){
    case "A":
        document.write("A is selected");
        break
    case "B":
        document.write("B is selected");
        break
    case "C":
        document.write("C is selected");
        break
    case "D":
        document.write("D is selected");
        break
    case "E":
        document.write("E is selected");
        break
    default:
        document.write("better luck next time");

}
```
- diffrence between switch and if else if statement
---
## An operators in javascript
- following operators supported in javascript
    - Arithemetic operators (` + , - , * , / , % , ** , ++ , -- `)
    - Assignment operators (` = , += , -= , *= , /= , %= , **=  `)
        - it will also return the value so we can print the value directly or store the value inside another variable
    - logical operators (` && , || , ! `)
    - comparision operators (` > , >= , < , <= , == , != , === , !==`)
    - special type of operators
    - bitwise oprators (` & , | , ^ , ~ , << , >> `)
    - ternary operators
---
- write a javascript code apply and post and pre increment and check the changes in single javascript file
- write a javascript code as we know assignment operator is meant for memory uitilization develop one meaningfull usecase
- write a javascript code 
    - a. bitwise and operator
    - b. bitwise or operator
    - c. bitwise exlusive or operator
    - d. birwise not(complement) operator
    - e. birwise left shift and right shift operator


---
### diffrence between == and === in js
- `==` is meant for content comparision 
- `===` is meant for data type content comparision 

---

