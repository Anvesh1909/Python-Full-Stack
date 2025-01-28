let loginBtn = document.getElementById("submitBtn");
let success = document.querySelectorAll("success");

console.log("HEllo")

function Login(){
    success.style.opacity = 100;
    console.log("Clicked");
}

loginBtn.addEventListener("click",Login)
