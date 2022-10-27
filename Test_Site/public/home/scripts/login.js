function Login(str,str2) {
    if (str.length == 0) {
      document.getElementById("txtHint").innerHTML = "";
      return;
    } else {
      const xmlhttp = new XMLHttpRequest();
      xmlhttp.onload = function() {
        document.getElementById("txtHint").innerHTML = this.responseText;
      }
    xmlhttp.open("POST", "..ogin?uname=" + str+"&psw="+str2);
    xmlhttp.send();
    }
  }

function GET_L(){
    if(str.length ==0){
        document.getElementById("KK").innerHTML="";
        return;
    }else{
        const xmlhttp = new XMLHttpRequest();
        xmlhttp.onload = function(){
            document.getElementById("KK").innerHTML = this.responseText;
        }
        xmlhttp.open("GET","../cgi-bin/login");
        xmlhttp.send();
    }
}