#!/usr/bin/python3
import os
os.system("clear")

while True:
    try:
        NAMES = ["Xavier","Daphne","Loki","Luci"]
        INP = input("Name: ")
        
    except ValueError as e:
        print("Your name is not in the list")