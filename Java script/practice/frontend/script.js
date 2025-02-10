// console.log("Javascript Linked");


let count = 0;

function btnClick(){
    count++;
    console.log(count);
}


let c = 0;
function openAlert(){
    c++;
    window.alert("button clicked "+c);
}




function add(){
    // by default promt will take string type
    // we need to type cast 
    // parseInt, parseFloat, 
    let a = parseInt(window.prompt("Enter a number:"));
    let b = parseInt(window.prompt("Enter another number:"));

    window.alert(a+b);
}


function confirmDialog(){
    window.confirm("Are you sure?");
}




function changeText(){
    let p = document.getElementById("text");
    // p.innerHTML = "text changed";
    p.append(" using html css js");
    // p.innerText = "text changed";
}