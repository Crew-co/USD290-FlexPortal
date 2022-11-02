#!/usr/bin/python3

import cgi, cgitb
import requests as rq
import os
import warnings as w
import json
import re

print("Content-Type: text/html")
print()

cgitb.enable()  # for debugging
form = cgi.FieldStorage()
name = form.getvalue("fname")
staff = form.getvalue("staff")
staffID = "ABC"

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
    except TypeError as e:
        print("No Name was Given")
def GETSTUDENT_EVENT(stu):
    if staffID == "ABC":
        try:
            # student = input("User: ")
            student = stu
            res = rq.get("https://flex.usd290.org/cyclonehour/admajax.php?search=" + student,verify=False,)
            NL = re.split("=|'>|</a>|<a href|Suggestions</div>\n<div class|</div>\n<div class|<div class|'suggest_link|'suggestions'|</div>\nError, invalid action|'adminStuProf.|php|uid|\?|style|'color: #08c;|No suggestions|''",res.text)
            NL_EMPTY_STRINGS = []
            for string in NL:
                if string != "":
                    NL_EMPTY_STRINGS.append(string)
                    if ' ' in NL_EMPTY_STRINGS:
                        NL_EMPTY_STRINGS.remove(' ')
                        #print("Person Not Found")
            #print(NL_EMPTY_STRINGS)
            out = NL_EMPTY_STRINGS.pop(0)
            STID = out
            start = "2022-10-10T00:00:00-05:00"
            end = "2022-11-15T00:00:00-05:00"
            data = {
                "studentID":STID,
                "start":start,
                "end":end
            }
            res = rq.post("https://flex.usd290.org/cyclonehour/eventFeed.php",data=data,verify=False)
            todos = json.loads(res.text)
            print("<link rel='stylesheet' href='styles.css'>")
            print("<table>")
            print("<tr>")
            print("<th>ID</th>")
            print("<th>Title</th>")
            print("<th>StaffID</th>")
            print("<th>Start</th>")
            print("<th>End</th>")
            print("</tr>")
            for entry in todos:
                print("<tr>")
                print(f"<td>{entry['id']}</td>")
                print(f"<td>{entry['title']}</td>")
                print(f"<td>{entry['staffid']}</td>")
                print(f"<td>{entry['start']}</td>")
                print(f"<td>{entry['end']}</td>")
                print("</tr>")
            print("</table>")
        except TypeError as e:
            print("No Name was Given")
        except IndexError as e:
            print("User Events Not found")
    else:
        print("FAIL")
def Get_Events_STAFF(SD):
    # staffID = input("ID: ")
    staffID = SD
    start = "2022-10-10T00:00:00-05:00"
    end = "2022-11-15T00:00:00-05:00"

    data = {"staffID": staffID, "start": start, "end": end}
    res = rq.post("https://flex.usd290.org/cyclonehour/eventFeed.php", data=data, verify=False)
    # print(res.text)
    todos = json.loads(res.text)
    print("<link rel='stylesheet' href='./home/styles.css'>")
    print("<table>")
    print("<tr>")
    print("<th>ID</th>")
    print("<th>Title</th>")
    print("<th>StudentID</th>")
    print("<th>Start</th>")
    print("<th>End</th>")
    print("</tr>")
    for entry in todos:
        print("<tr>")
        print(f"<td>{entry['id']}</td>")
        print(f"<td>{entry['title']}</td>")
        print(f"<td>{entry['studentID']}</td>")
        print(f"<td>{entry['start']}</td>")
        print(f"<td>{entry['end']}</td>")
        print("</tr>")
    print("</table>")
        #print("<p>"+"|"+ entry["id"]+ " "+ entry["title"]+ " "+ entry["studentID"]+ " "+ entry["start"]+ " "+ entry["end"]+"</p>")

#GETSTUDENT_EVENT(name)
#GETSTUDENT(name)
if name != None:
    LT = name.split()
    if len(LT) == 2:
        n1 = LT[0]
        n2 = LT[1]
        GETSTUDENT_EVENT(n1+n2)
    elif len(LT)==1:
        GETSTUDENT(name)
elif staff != None:
        Get_Events_STAFF(staff)
else:
    print("Nothing was given")