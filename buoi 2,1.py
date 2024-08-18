# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:20:16 2024

@author: HP
"""

distance= float(input("Diem trung binh GPA:"))
if distance < 3.5:
    print("Hoc luc kem")
elif 3.5 <= distance<5:
    print("hoc luc yeu")
elif distance >=5 and distance<7:
     print("hoc luc trung binh")
elif distance>= 7 and distance<8:
    print("hoc luc kha")
elif distance>=8 and distance<9:
    print("hoc luc gioi")
elif distance>=9 and distance<= 10:
    print("hoc luc xuat sac")
else:
    print("khong xac dinh")
    
    
    
    
    