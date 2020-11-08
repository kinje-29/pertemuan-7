# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:47:58 2020

@author: anshar
"""

gaji = int(input("MASUKAKAN GAJI :"))
berkeluarga = (False, True) [input("sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True) [input("punya rumah? (Y/T)") == "Y"]


if gaji > 3000.000 :
    print("Gaji Sudah Di Atas UMR")
if berkeluarga :
    print("Wajib Ikut Asuransi Dan Ikut Pensiun")
else :
    print("Tidak perlu ikut asuransi")
if punya_rumah :
    print("wajib bayar pajakk rumah")
else:
    print("Tidak wajib bayar pajak rumah")
    print("Gaji belum UMR")
    










