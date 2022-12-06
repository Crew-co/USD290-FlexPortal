#!bin/python3
from cryptography.fernet import Fernet
import json

# Opening Json file
f = open('Encrypted.json','rb')
LJ = json.load(f)
f.close()

k = open('fk.key','rb')
key = k.read()
k.close()

fern = Fernet(key)

enc = fern.encrypt(LJ)

A = open('Encrypted.json','wb')
A.write(enc)
A.close()