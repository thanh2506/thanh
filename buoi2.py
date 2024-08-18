# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 06:58:22 2024

@author: HP
"""

distance= float(input("Nhap do dai doan duong den truong(m)"))
if distance<300:
    print("duong den truong qua gan. thoi! di bo")
elif distance > 1200:
    print("duong den truong qua xa. THOI! di xe may ")
elif distance >= 300 and distance <= 700:
    print("duong den truong khong xa. thoi di xe dap")
else:
    print("khong xac dinh")