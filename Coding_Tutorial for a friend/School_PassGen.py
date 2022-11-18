#!/usr/bin/python3
from random import randint as r
import json
from os.path import exists
import os
from getpass import getpass


def Pass_Lib_Gen():
    P1 = []
    #RD = []
    for i in range(10000):
        Base0 = "154"
        Base1 = "155"
        Base2 = "156"
        Base3 = "157"
        Base4 = "158"
        Base5 = "159"
        I = r(111,999)
        out0 = Base0+str(I)
        out1 = Base1+str(I)
        out2 = Base2+str(I)
        out3 = Base3+str(I)
        out4 = Base4+str(I)
        out5 = Base5+str(I)        

        if out0 or out1 or out2 or out3 or out4 or out5 not in P1:
            P1.append(out0)
            P1.append(out1)
            P1.append(out2)
            P1.append(out3)
            P1.append(out4)
            P1.append(out5)

    P1 = list(set(P1))

    with open('Passwds.json','wb') as f:
        SORT = sorted(P1)
        jsonString = json.dumps(SORT)
        f.write(jsonString.encode())  
    f.close()
Pass_Lib_Gen()

def Pass_Check(A):
    FE = exists('Passwds.json')
    if FE == False:
        Pass_Lib_Gen()
    else:
        f = open('Passwds.json')
        LJ = json.load(f)
        f.close()

        if A in LJ:
            #INX = LJ.index(A)
            #ot = LJ.pop(INX)
            #print(f"Found {ot} at index {INX}")
            print("Password Found!!!")

Pass_Check(A=getpass("Check if Paswd is in List: "))