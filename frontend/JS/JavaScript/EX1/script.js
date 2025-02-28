    // console.log("Linked");

    // document.write("linked");



    // document.getElementById("dropmenu").style.display = "block";

    let dropButtom = document.getElementById("dropmenu");

    function dropBtn(){
        // console.log("Btn clicked");
        if(dropButtom.style.display == "block"){
            dropButtom.style.display = "none";
        } else{
            dropButtom.style.display = "block";
        }
    }