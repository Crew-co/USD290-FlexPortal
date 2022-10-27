#!/usr/bin/python3
import os
os.system("clear")

while True:
    try:
        NAMES = ["Xavier","Daphne","Loki","Luci"]
        INP = input("Name: ")
        #YOUR CODE HERE
        

    except ValueError as e:
        print("Your name is not in the list")