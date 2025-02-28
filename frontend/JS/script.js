function bitwise(){
    let a = 3;
    let b = 1;
    console.log(a&b);
    console.log(a|b);
    console.log(a^b);
    console.log(~a);

    console.log("\npower of 2's using left shift");
    let p = 1;
    for(let i = 0; i<10 ; i++){
        console.log(p<<i);
    }

    console.log("\n16>>2");
    console.log(16>>2);
}

bitwise()


// let a = "5"%2;

// console.log(a);
// console.log(typeof(a));