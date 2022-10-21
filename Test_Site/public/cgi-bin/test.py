#!/usr/bin/python3
import cgi, cgitb
cgitb.enable() # for debugging
form = cgi.FieldStorage()
CMD = form.getvalue("cmd")
print("Content-Type: text/html;charset=utf-8")
print()
