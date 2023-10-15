
const signInData = {
    firstName: "",
    lastName: "",
    email: "",
    age: 0,
    pwd: "",
    signed: false,
}

const startButton = document.querySelector("button#start");
const signInChoice = document.querySelector("form#signin-choice")
const signInForm = document.querySelector("form#sign-in");
const signIn = document.querySelector("button#start-signin");
const createAccount = document.querySelector("button#start-create-account");
const createAccountForm = document.querySelector("form#create-account");
const skip = document.querySelector("button#start-skip");

const signInSubmit = document.querySelector("button#signin");

function start() {
    // console.log(startButton);
    if (signInData.signed === true) {
        alert("signed in");
        startButton.style.display = 'none';
    }
    else {
        // alert("sign in page");
        startButton.style.display = 'none';
        signInChoice.style.display = 'block';
        signIn.addEventListener('click', function(event) {
            // alert("yea");
            event.preventDefault();
            signInChoice.style.display = 'none';
            signInForm.style.display = 'block';
            signInForm.addEventListener('submit', function(event) {
                event.preventDefault();
                const username = document.getElementById("username").value;
                const password = document.getElementById("password").value;
                console.log(`User Name: ${username}\n Pwd: ${password}`);
                // from here make GET request to api
            })
        });
        createAccount.addEventListener('click', function(event) {
            // alert("create account");
            accountData = {}

            event.preventDefault()
            signInChoice.style.display = 'none';
            signInForm.style.display = 'none';
            createAccountForm.style.display = 'block';
            createAccountForm.style.width = '450px';
            createAccountForm.addEventListener('submit', function(event) {
                event.preventDefault();
                firstName = document.getElementById("first_name");
                lastName = document.getElementById("Last_name");
                email = document.getElementById("email");
                birthDate = document.getElementById("dob");
                gender = document.getElementById("gender");
                newPwd = document.getElementById("password");
                confirmPwd = document.getElementById("confirm-password");

                accountData = {
                    "first_name": firstName.value,
                    "last_name": lastName.value,
                    "email": email.value,
                    "dob": birthDate.value,
                    "gender": gender.value,
                    "password": newPwd.value
                };
                data = JSON.stringify(accountData);
                console.log(accountData);
                // api POST request fro here

                url = "http://127.0.0.1:5005/api/v1/users/";

                fetch(url, {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: data
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                    })
                    .catch(error => {
                        console.log("Error:", error);
                    });

            })
        });
        skip.addEventListener('click', function(event) {
            // alert("skip");
            event.preventDefault();
            signInChoice.style.display = 'none';
            // createAccountForm.style.display = 'block';
            startButton.style.display = 'block';
        });
    }
}