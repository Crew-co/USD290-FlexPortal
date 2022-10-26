#!/usr/bin/python3
from periodictable import *
from math import ceil
import periodictable as pt
#RULES
# P --> Moles /
# Moles --> Mass *
# Mass ---> Moles /
# Moles to P --> *
#AVGN = 6.02*10**23
#EOF

AVG = 6.02*10**23

def Convert(IN1,IN2,IN3):
    if IN1 == "PTM":
        SUM = float(IN2) / AVG
        print(SUM)
    elif IN1 == "MTM":
        SUM = float(IN2)*float(IN3)
        print(SUM)
    elif IN1 == "MSTM":
        SUM = IN2 / IN3
        print(SUM)
    elif IN1 == "MTP":
        SUM = IN2 * IN3
        print(SUM)

def GM(IN1,IN2,IN3,IN4,IN5,IN6):
    ADDON = ".mass"
    LST = [IN1,IN2,IN3]
    if None in LST:
        LST.remove(None)
    
    LNST = len(LST)
    if LNST == 2:
        A = LST.pop(0)
        B = LST.pop(0)
        JN1 = ''.join("pt."+IN1+ADDON)
        JN2 = ''.join("pt."+IN2+ADDON)
        #print(JN1+" "+" "+JN2)
        op1 = "*"
        op2 = "+"
        T1 = eval(JN1)
        T2 = eval(JN2)
        SUM1 = T1 * IN4
        SUM2 = T2 * IN5
        TSUM = SUM1 + SUM2
        print(round(TSUM,2))
    elif LNST == 3:
        A = LST.pop(0)
        B = LST.pop(0)
        JN1 = ''.join("pt."+IN1+ADDON)
        JN2 = ''.join("pt."+IN2+ADDON)
        JN3 = ''.join("pt."+IN3+ADDON)
        #print(JN1+" "+" "+JN2)
        op1 = "*"
        op2 = "+"
        T1 = eval(JN1)
        T2 = eval(JN2)
        T3 = eval(JN3)
        SUM1 = T1 * IN4
        SUM2 = T2 * IN5
        SUM3 = T3 * IN6
        TSUM = SUM1 + SUM2 + SUM3
        print(round(TSUM,2))
    else:
        print(f"NO LEN OF LIST: {LNST}")

def Main():
    F = None
    print("Type C to Convernt or M to Calculate Mass ")
    I = input("ADMIN@SERVER> ")
    if I == "C":
        print("Convert Menu")
        print("What are you wanting to convert")
        print("Grams to Mass, Mass to Grams, Particals to Moles or Moles to Particals?")
        print("Type PTM,MTM,MSTM,MTP to continue")
        print("Ie PTM Num1,Num2")
        INP = input("Convert> ")
        V = INP.split()
        if len(V)==2:
            Convert(V[0],V[1],F)
        else:
            Convert(V[0],V[1],V[2])
    elif I == "M":
        print("Calculate Mass")
        M = input("CM> ")
        V = M.split()
        
Main()
