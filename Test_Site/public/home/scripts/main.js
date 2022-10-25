function Login(){
    var list = ['admin','password'];
    alert("Please enter your creds to continue");
    if (prompt("Enter Username")=="admin"){
        if (prompt("Enter Password")=="password"){
            alert('You are now Logged in.')
        }else{
            fail()
        }
    }else{
        fail()
    }

}

function fail(){
    alert('Fail Try again')
    Login()
}