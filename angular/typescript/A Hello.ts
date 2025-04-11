console.log("Hello world!");




var a:number = 10;
console.log("a = "+a);




var pid:number = 1001;
var pname:string = "mobile1";
var price:number = 9999.99; 

console.log(pid,pname,price);





var productDetails:any = [1001,"mobile1",9999.99];
console.log(productDetails);





function hello(){
    console.log("Hello function in type script");
}

hello()




function empFunction(eid:number,ename:string,esal:number){
    console.log("\n\nWith formal parameters\n")
    console.log("eid : ",eid);
    console.log("ename : ",ename);
    console.log("esal : ",esal);
}

empFunction(101,"Anvesh",20000.00);





function empFunction2(eid:number=101,ename:string="Anvesh",esal:number=5000){
    console.log("\n\nWith default parameters\n")
    console.log("eid : ",eid);
    console.log("ename : ",ename);
    console.log("esal : ",esal);
}

empFunction2();





function Add(a:number,b:number){
    console.log("\n\nAdd function\n");
    return a+b;
}

console.log(Add(10,20));



function Add1(...argv){
    console.log("\n\n rest parameter add operation \n")
    let sum:number = 0;
    for (let i = 0; i < argv.length; i++) {
        sum += argv[i];
    }
    return sum;
}

console.log(Add1(1,2,3,4,5));





class Student{
    constructor(){
        console.log("\n\nNon parameterized construstor")
    }
}

let s1 = new Student();

class Student2{
    constructor(){
        console.log("\n\nparameterized construstor")
    }
}

let s2 = new Student2();