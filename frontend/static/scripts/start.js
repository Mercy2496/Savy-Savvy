
function apiGetReady(){
    const url = "http://127.0.0.1:5005/api/v1/"

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            var key = Object.keys(data);
            const logo = document.querySelector(".logo img")
            if (data[key] == "SUCCESS") {
                // console.log(logo);
                logo.id = "ready";
                console.log("API: ", data[key]);
            }
            else {
                logo.id = "not-ready";
                console.log("API: ", "FAILED");
            }
        })
        .catch(error => {
            console.log("API: ", "FAILED");
            console.log("Error:", error);
        });
}
apiGetReady();


const signInData = {
    firstName: "",
    lastName: "",
    email: "",
    age: 0,
    gender: "",
    pwd: "******",
    signed: false,
}

const redSignIn = document.querySelector("div.accounts");
const user = document.querySelector("div.logged-in");
const userLogo = document.querySelector("div.logged-in img");
const startButton = document.querySelector("button#start");
const signInChoice = document.querySelector("form#signin-choice")
const signInForm = document.querySelector("form#sign-in");
const signIn = document.querySelector("button#start-signin");
const createAccount = document.querySelector("button#start-create-account");
const createAccountForm = document.querySelector("form#create-account");
const skip = document.querySelector("button#start-skip");

const signInSubmit = document.querySelector("button#signin");
const startLink = document.getElementById('startLink');

function start() {
    // console.log(startButton);
    if (signInData.signed === true) {
        // alert("signed in");
        startButton.textContent = "Explore";
        window.location.href = "http://127.0.0.1:5000/display";
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
            // signingIn();
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
                        createAccountForm.style.display = 'none';
                        startButton.style.display = 'block';

                        popup = document.querySelector("div.success-popup");
                        popup.style.display = "block"
                        console.log(popup);
                        popup.classList.add("open-popup");
                        // startButton.style.display = "none";

                        signNow = document.querySelector("button#sign-now");
                        // console.log(signNow);
                        signNow.addEventListener('click', function(event) {
                            popup.classList.remove("open-popup");
                            startButton.style.display = 'none';
                            signInForm.style.display = 'block';
                        });
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
            signInData.signed = true;
        });
    }
}

function signingIn() {
    signInfo = {}
    signInForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("pwd").value;
        console.log(`Name: ${username}\nPwd: ${password}`);
        // from here make GET request to api
        signInfo["email"] = username;
        signInfo["password"] = password;
        console.log(signInfo);
        // alert("Signing in now!");
        url = "http://127.0.0.1:5005/api/v1/user"

        fetch(url, {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(signInfo)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            let status = false;
            keys = Object.keys(data);
            // console.log(keys);
            for (const key of keys) {
                // console.log(key)
                if (["email", "first_name", "last_name"].includes(key)) {status=true}
                else if (["user"].includes(key)) {
                    if (data[key] === "forgot_pwd") {
                        status = "forgotPwd";
                    }
                    if (data[key] === false) {
                        status = false;
                    }
                }
            }
            console.log(status);
            if (status === true) {
                signInData.firstName = data["first_name"];
                signInData.lastName = data["last_name"];
                signInData.email = data["email"];
                signInData.gender = data["gender"]
                signInData.signed = true;
                startButton.textContent = "Explore";

                console.log(redSignIn);
                console.log(user);
                console.log(userLogo);
                redSignIn.style.display = "none";
                if (["male", "Male"].includes(signInData.gender)) {
                    userLogo.src = "../static/images/male-acc";
                }
                else if (["female", "Female"].includes(signInData.gender)) {
                    userLogo.src = "../static/images/female-acc";
                }
                else if (["lgbtq", "LGBTQ"].includes(signInData.gender)) {
                    userLogo.src = "../static/images/lgbtq.jpg"
                }
                else {
                    userLogo.src = "../static/images/other.png"
                }
                user.style.display = "inline-block";
                signInForm.style.display = "none";
                startButton.style.display = "block";

            }
            else if (status === false) {
                alert("You don't have an account yet");
            }
            else {
                alert("Incorrect password");
            }
        })
        .catch(error => {
            console.log("Error:", error);
        });


        })
}
signingIn();