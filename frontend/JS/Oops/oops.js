class Students{
    // non parameterized constructor
    constructor(){
        console.log('Student Constructor');
    }



}

let s1 = new Students();
let s2 = new Students();


class Student_details{   

    // parameterized constructor
    constructor(name,age,marks){
        this.name = name;
        this.age = age;
        this.marks = marks;
        console.log(this.name,this.age,this.marks);
    }

    showDetails(){

        let details = `my name is ${this.name} \nmy age is ${this.age} \nmy marks is ${this.marks}`;

        console.log(details);
    }

}


let s3 = new Student_details("Anvesh",22,55);

console.log(s3.name);
console.log(s3.age);
console.log(s3.marks);

s3.showDetails();



class Student_static_exe{

    constructor(){
        this.constructor.static_exe();
    }

    static static_exe(){
        console.log("Static method");
    }

    instanceMethod(){
        Student_static_exe.static_exe();
        this.constructor.static_exe();
    }
}

let s4 = new Student_static_exe();
s4.instanceMethod()
// s4.static_exe() not possible


Student_static_exe.static_exe();




class Parent{

    constructor(){
        console.log('Parent Constructor');
    }

    pMethod(){
        console.log("Parent method");
    }
}

class Child extends Parent{

    // constructor(){
    //     console.log('Child Constructor');
    // }

    cMethod(){
        console.log("Child method");
    }
}


let c = new Child();
c.pMethod();
c.cMethod();





// polymorphism
class A{
    constructor(){
        console.log("A constructor");
    }

    m1(){
        console.log("A class implementation");
    }
}

class B extends A{

    
    constructor(){
        console.log("B constructor");
    }

    m1(){
        console.log("B class implementation");
        super.m1()
    }

}


let b = new B();
b.m1();


