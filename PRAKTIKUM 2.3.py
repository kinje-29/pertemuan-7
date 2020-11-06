# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:12:13 2020

@author: anshar
"""

print("masukan bilangan yang di inginkan")
def pengulangan():
    a = int(input("bilangan1 ="))
    b = int(input("bilangan2 ="))
    c = int(input("bilangan3 ="))
    
    if a>b and a>c:
        if b>c:
           print (a, "terbesar dan", c, "terkecil")
        else:
           print(a, "terbesar dan", b, "terkecil")
    elif b>a and b>c:
        if a>c:
           print(b, "terbesar dan", c, "terkecil")
        else:
           print(b, "terbesar dan", c, "terkecil")
    else:
        if a>b:
            print(c, "terbesar dan", a, "terkecil")
        else:
            print(c,"terbesar", a, "terkecil")

    print ("")
    print("ingin coba lagi? (ya/tidak)")
    x=input()
    if x== "ya":
     return pengulangan()
    if x== "tidak":
        print("apakah sudah mengerti?")

pengulangan()


































