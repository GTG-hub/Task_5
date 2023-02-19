var csrf = document.getElementById('csrf').value
console.log("")


function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    
    if(username == '' && password==''){
        alert("Please enter username and password")
    }
    var data = {
        'username' : username,
        'password' : password
    }
    fetch('/api/login/'), {
        method : 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf

        },
        'X-CSRFToken' : csrf,
        'body' : JSON.stringify(data)

    }
}