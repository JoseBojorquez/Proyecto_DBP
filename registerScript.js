const registerBtn = document.querySelector(".btn");
const email = document.getElementById("form1");
const firstname = document.getElementById("form2");
const lastname = document.getElementById("form3");
const password = document.getElementById("form4");
const confirmpassword = document.getElementById("form5");

registerBtn.addEventListener("click",post);

function post(){
    if(email.value != null && firstname.value != null && lastname.value != null && password.value != null && confirmpassword.value != null){
        if(isEmpty(email.value) == 0 && isEmpty(firstname.value) == 0 && isEmpty(lastname.value) == 0 && isEmpty(password.value) == 0 && isEmpty(confirmpassword.value) == 0){
            if(password.value == confirmpassword.value){
                postUser();
            }
        }
    }
}

function isEmpty(str) {
    return !str.trim().length;
}

async function postUser() {
    const response = await fetch("http://localhost:8000/users/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: `{
            "email": "${email.value}",
            "password": "${password.value}",
            "firstname": "${firstname.value}",
            "lastname": "${lastname.value}"
        }`,
    });

    response.json().then(data => {
        console.log(JSON.stringify(data));
    });
}