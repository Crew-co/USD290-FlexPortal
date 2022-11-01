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
        SUM = float(IN2) / float(IN3)
        print(SUM)
    elif IN1 == "MTP":
        SUM = float(IN2) * AVG
        print(SUM)
    elif IN1 == "PTM2":
        SUM = eval(IN2) / AVG
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
        #print(JN1)
        JN2 = ''.join("pt."+IN2+ADDON)
        #print(JN2)
        #print(JN1+" "+" "+JN2)
        op1 = "*"
        op2 = "+"
        T1 = eval(JN1)
        T2 = eval(JN2)
        SUM1 = float(T1) * IN4
        SUM2 = float(T2) * IN5
        TSUM = SUM1 + SUM2
        print(round(TSUM,2))
    elif LNST == 3:
        A = LST.pop(0)
        B = LST.pop(0)
        JN1 = ''.join("pt."+IN1+ADDON)
        #print(JN1)
        JN2 = ''.join("pt."+IN2+ADDON)
        #print(JN2)
        JN3 = ''.join("pt."+IN3+ADDON)
        #print(JN3)
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
        print("Ie CM> Elem1 Elem2 Num1 Num2/ Elem1 Elem2 Elem3 Num1 Num2 Num3")
        M = input("CM> ")
        V = M.split()
        print(len(V))
        if len(V) == 4:
            #print(V[0],V[1],V[2],V[3])
            GM(V[0],V[1],F,int(V[2]),int(V[3]),F)
        elif len(V) == 6:
            GM(V[0], V[1], V[2], int(V[3]), int(V[4]), int(V[5]))   
#Main()

def AllC():
    F = None
    print("Ie CM> Elem1 Elem2 Num1 Num2/ Elem1 Elem2 Elem3 Num1 Num2 Num3")
    M = input("CM> ")
    V = M.split()
    if len(V) == 4:
        A = GM(V[0],V[1],F,int(V[2]),int(V[3]),F)
        return A
    elif len(V) == 6:
        B = GM(V[0], V[1], V[2], int(V[3]), int(V[4]), int(V[5]))
        return B
    elif len(V) == 2:
        C = GM(V[0], F, F, int(V[1]),F,F)
        return C

def All(IN2,IN3):
    ELM = AllC()
    print("What conversion are u wanting to do?")
    print("PTM,MTP,MTM,MSTM,MTP")
    print("Ie PTM num1, num2")
    LST = ["PTM","MTM","MSTM","MTP"]
    EV = input("PTM2: ")
    if EV == "":
        for IN in LST:
            A = Convert(IN, IN2, IN3)
            print(IN + " " +A)
    else:
        LST.append(EV)
        for IN in LST:
            B = Convert(IN, IN2, IN3)
            print(B)
    return A

def M2():
    A = input("Num1: ")
    B = input("Num2: ")
    All(A,B)

#M2()












# 1 2 3
# 4 5 6
# 7 8 9
#   0