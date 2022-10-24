#!/usr/bin/python3
print("Content-Type: text/html")
print()

import cgi, cgitb

cgitb.enable()  # for debugging
form = cgi.FieldStorage()
usr = form.getvalue("uname")
psw = form.getvalue("psw")

print(usr)
print(psw)