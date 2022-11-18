#!/usr/bin/python3
from random import randint as r

P = []

while True:
    RND = r(1,7)
    out = f"01{RND}21"
    if out not in P:
        P.append(out)
    if len(P)==7:
        break
    else:
        pass
print(P)

    