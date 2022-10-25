function login(){
    alert("Enter your login creds to continue")
    if(prompt("Username").includes("admin")){
        if(prompt("Password")=="password"){
            return true
        }else{
            alert("Try again")
            fail()
        }
    }
}

function fail(){
    login()
}

function start(){
    if(login()==true){
        var command = prompt("Command")
        var rtn =$.post("https://8001-crewco-usd290flexportal-t4pccm2pppy.ws-us71.gitpod.io/cgi-bin/test",{
            cmd: command
        });
    }
    alert(rtn)
}

start()