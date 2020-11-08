# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:17:33 2020

@author: anshar
"""

baris = 10
kolom =baris

for x in range(baris):
    for y in range(kolom):
        menambah = x + y
        print("{0:>5}".format(menambah),end='')
    print()
        
        
        