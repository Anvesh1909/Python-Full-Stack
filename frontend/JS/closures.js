// closures in js is nothing but innerfunction or nested function which can be 
// represented as defining or declaring a function inside an another function then it is said to be cloures

function outerfunction(){
    console.log("outer function");
    function innerfunction(){
        console.log("inner function");
    }
    innerfunction()
}

outerfunction()



// write a javascript code develop 2 meaningful usecases for closures in javascript 
