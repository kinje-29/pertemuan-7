# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:54:31 2020

@author: anshar
"""
## LATIHAN 1 MENENTUKA NILAI AKHIR ##
nama   =input("masukan nama: ") 
uts    =input("masukan nilai UTS: ")
uas    =input("masukan nilai UAS: ")
tugas  =input("masukan nilai TUGAS: ")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
keterangan = ("TIDAK LULUS" , "LULUS") [akhir > 60.0]
 
if akhir > 80 :
    huruf = "A"
elif akhir > 70 :
    huruf = "B"
elif akhir > 50 :
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "ANDA BELUM BERUNTUNG"

print ("\nNama: " , nama)
print ("NILAI UTS: " , uts)
print ("NILAI UAS: " , uas)
print ("NILAI TUGAS: " , tugas)
print ("NILAI AKHIR: " , akhir)
print ("\nNILAI HURUF: " , huruf)
print ("KETERANGAN : " , keterangan)


