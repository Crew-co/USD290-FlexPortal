#!bin/python3
from cryptography.fernet import Fernet
import json

# Opening Json file
f = open('Encrypted.json')
LJ = json.load(f)
f.close()

k = open('fk.key')
R = k.readlines()
k.close()