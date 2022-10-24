function GETSTUDENT(str) {
    if (str.length == 0) {
      document.getElementById("txtHint").innerHTML = "";
      return;
    } else {
      const xmlhttp = new XMLHttpRequest();
      xmlhttp.onload = function() {
        document.getElementById("txtHint").innerHTML = this.responseText;
      }
    xmlhttp.open("GET", "/cgi-bin/student_form?fname=" + str);
    xmlhttp.send();
    }
  }

function GETSTAFF(str) {
    if (str.length == 0) {
      document.getElementById("txtHint").innerHTML = "";
      return;
    } else {
      const xmlhttp = new XMLHttpRequest();
      xmlhttp.onload = function() {
        document.getElementById("txtHint").innerHTML = this.responseText;
      }
    xmlhttp.open("GET", "/cgi-bin/student_form?staff=" + str);
    xmlhttp.send();
    }
  }