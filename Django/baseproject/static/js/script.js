function clickMe(){
    window.alert("Hello World!");
}


function login(){
    // alert("HEllo");
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;
    if(user == ""){
        document.getElementById("usererror").innerHTML ="invalid username";
        return false;
    }
    if(pass==""){
        document.getElementById("passerror").innerHTML ="invalid password";
        return false;
    }
}