

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
        new A();
        console.log("B constructor");
    }

    m1(){
        console.log("B class implementation");
        super.m1()
    }
}


let b = new B();
b.m1();


