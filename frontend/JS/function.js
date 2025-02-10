function test(){
    console.log("Welcome to functions in javascript");
}

test()
test()
test()


// name full function
// defalut paraments b
function add(a,b=0){
    return a+b
}

// formal paraments 
console.log(add(10,30))
// keyword arguments
console.log(add(b=10,a=70))
// using default parameter
console.log(add(70))
// a= NaN or undefined
console.log(add())





// name less function 
let hello = function(){
    console.log("hello world!");
}
hello()






let arrow = () => {
    console.log("HELLO ARROW FUNCTION")
}

arrow()



let returnEx = () => {
    return "Return function"
}

console.log(returnEx())




