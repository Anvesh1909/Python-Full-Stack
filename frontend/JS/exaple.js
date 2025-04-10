// // sum of a array
// function sumOfArray(arr){
//     let sum = 0;
    
//     // for(let i=0; i<arr.length; i++){
//     //     sum += arr[i];
//     // }

//     for(let i of arr){
//         sum += i
//     }

//     return sum;
// }

// let a = [1,2,3,4,5];
// // console.log(sumOfArray(a));
// let s = sumOfArray(a);
// console.log(s);


/*

class Abc:
    def __init__(self):
        print("Abc Constructor")

o1 = Abc()

*/

// ex1
// class Abc{
//     constructor(){
//         console.log("ABC constructor");
//     }
// }

// let o1 = new Abc();


/*

class Abc:
    def __init__(self):
        self.name = "Anvesh"
        print("Abc Constructor")
    def method1(self):
        print("Abc method1")
        print("my name is: ",self.name)
o1 = Abc()
o1.method1()

*/


// // ex2
// class Abc{
//     constructor(){
//         this.name = "Anvesh";
//         console.log("ABC constructor");
//     }
//     //instance method
//     method1(){
//         console.log("Abc Method1");
//         console.log("My name is: ",this.name);
//     }
// }

// let o1 = new Abc();
// o1.method1()



// // ex3
// class Abc{
//     constructor(name){
//         this.name = name;
//         console.log("ABC constructor");
//     }
//     //instance method
//     method1(){
//         console.log("Abc Method1");
//         console.log("My name is: ",this.name);
//     }
// }

// let o1 = new Abc("Anvesh");
// o1.method1()

// let o2 = new Abc("paaaranaaaa");
// o2.method1()





/*

class Abc:
    def __init__(self):
        self.name = "Anvesh"
        print("Abc Constructor")
    def method1(self):
        print("Abc method1")
        print("my name is: ",self.name)

    @staticmethod
    def staticMethod():
        print("Static method")

o1 = Abc()
o1.method1()

*/


// // ex4
// class Abc{

//     constructor(name){
//         this.name = name;
//         console.log("ABC constructor");
//     }

//     //instance method
//     method1(){
//         console.log("Abc Method1");
//         console.log("My name is: ",this.name);
//     }

//     // static method
//     static staticMethod(){
//         console.log("Static method");
//     }
// }

// let o1 = new Abc("Anvesh");
// o1.method1()

// // o1.staticMethod();   error static method cannot be called using object reference
// Abc.staticMethod();






// // ex4
// // class is nothing but a attributes and methods 
// class Abc{

//     // attributes 
//     head = "AnveshPrerana";

//     // methods
//     constructor(name){
//         this.name = name;
//         console.log("ABC constructor");
//     }

//     //instance method
//     method1(){
//         console.log("Abc Method1");
//         console.log("My name is: ",this.name);

//         console.log(this.head);
//     }

  
// }

// let o1 = new Abc("Anvesh");
// o1.method1()




class Mathamatics{

    // polymorphism
    // method overloading
    // varible length parameter
    // def add(*args)
    add(...args){

        let sum = 0;
        for(let i of args){
            sum += i
        }
        return sum;
    }

    sub(a,b){
        return a-b;
    }

    mul(a,b){
        return a*b;
    }

    div(a,b){
        if(b==0){
            return false;
        }
        return a/b;
    }
}

let a = new Mathamatics();

console.log(a.add(10,20,30,40,50,60));

console.log(a.div(10,2));

console.log(a.div(10,20));




class Anvesh{
    static childs(...c){

    }
}

