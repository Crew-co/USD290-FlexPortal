#!/usr/bin/python3
print("Content-Type: text/html")
print()

import cgi, cgitb
import requests as rq
import re

cgitb.enable()  # for debugging
form = cgi.FieldStorage()
name = form.getvalue("fname")


def GETSTUDENT(stu):
    try:
        # student = input("User: ")
        student = stu
        res = rq.get(
            "https://flex.usd290.org/cyclonehour/admajax.php?search=" + student,verify=False,
        )
        NL = re.split("=|'>|</a>|<a href|Suggestions</div>\n<div class|</div>\n<div class|<div class|'suggest_link|'suggestions'|</div>\nError, invalid action|'adminStuProf.|php|uid|\?|style|'color: #08c;|No suggestions|''",res.text)
        NL_EMPTY_STRINGS = []
        for string in NL:
            if string != "":
                NL_EMPTY_STRINGS.append(string)
                if ' ' in NL_EMPTY_STRINGS:
                    NL_EMPTY_STRINGS.remove(' ')
                    print("Person Not Found")
        for LST in NL_EMPTY_STRINGS:
            print("<ul>")
            print(f"<li>{LST}</li>")
            print("</ul>")
        print("<a href=/>Back</a>")
    except TypeError as e:
        print("No Name was Given")
        print("<a href=/>Back</a>")


GETSTUDENT(name)
