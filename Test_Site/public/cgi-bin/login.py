#!/usr/bin/python3
print("Content-Type: text/html")
print()

import cgi, cgitb

cgitb.enable()  # for debugging
form = cgi.FieldStorage()
usr = form.getvalue("uname")
psw = form.getvalue("psw")

if usr == "Admin":
    if psw == "password":
        print("<script>window.location.href = '/';</script>")
    else:
        print(f"<script>alert('Wrong username or password {psw}')</script>")
        print("<script>window.location.href='/admin';</script>")
else:
    print("<script>alert('Wrong Username')</script>")
    print("<script>window.location.href='/admin';</script>")