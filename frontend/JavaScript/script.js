// console.log("Hello World!");


// var a = 10;
// let b = 10;
// const c = 10;

// a = 20;
// console.log(a);
// b = 20;
// console.log(b);
// // c = 20;
// // console.log(c);




// // primitive data type
// let i = 20;
// let f = 3.14;
// let s = "ABC";
// let b1 = true;
// let b2 = false;
// let n = null;
// let u;

// console.log(typeof(i));
// console.log(typeof(f));
// console.log(typeof(s));
// console.log(typeof(b1));
// console.log(typeof(b2));
// console.log(typeof(n));
// console.log(typeof(u));








// function typeOfNumber(n){
//     if(n%2==0){
//         console.log(n,"is even number");
//     } else{
//         console.log(n,"is odd number");
//     }
// }

// typeOfNumber(10);
// typeOfNumber(11);





// // can be accecable thought out the file
// var v = 10;  // global variable 
// let l = 20;  //local variable
// const c = 30; // local varible

// function dummy(){
//     console.log("inside the function ",v,l,c)
// }

// console.log("outside the function ",v,l,c)
// dummy()







// function foo() {
//     var x = 1;
//     function bar() {
//       var y = 2;
//       console.log(x); // 1 (function `bar` closes over `x`)
//       console.log(y); // 2 (`y` is in scope)
//     }
//     bar();
//     console.log(x); // 1 (`x` is in scope)
//     console.log(y); // ReferenceError, `y` is scoped to `bar`
// }
  
// foo();







// function dunny(){
//     if(true){
//         var a = 20;
//         let b = 20;
//     }
//     console.log(a);
// }

// dunny()
// // console.log(a)





// for(let i=0 ; i<=9 ; i+=2){
//     console.log(i)
// }



// let i = 0;
// while(i<=9){
//     console.log(i);
//     i+=1;
// }






// sqroot 2 -> 2^(1/2) 
// cuberoot 2  -> 2^(1/3)  
// def isPrime():
//     for i in range(2,int(n**0.5)):
//     if n%i==0:
//         return False
//     return True


// 

// function isPrime(n){
//     for(let i=2; i< parseInt(n**(0.5)) ; i+=1){
//         if(n%i==0){
//             return false;
//         }
//     }
//     return true;
// }

// console.log(isPrime(11));
// console.log(isPrime(10));





// function sumOfDigit(n){
//     let s = 0;
//     while(n>0){
//         a = n%10;
//         s+=a;
//         n = parseInt(n/10);
//     }
//     return s;
// }

// console.log(sumOfDigit(1234))

// 101/10 -> 10.1 int(10.1) = 10




// function reverseOfNumber(n){
//     let rn = 0;
//     while(n>0){
//         a = n%10;
//         rn = rn*10+a;
//         n = parseInt(n/10);
//     }
//     return rn;
// }

// console.log(reverseOfNumber(1234));













