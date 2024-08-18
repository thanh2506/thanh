# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:30:06 2024

@author: HP
"""

print("tinh tien so km di duoc")
a=float(input("nhap so km di duoc:"))
if a<=1:
    print("so tien cua ban la 20k")
elif a<=4:
    d=a*13000
    print("so tien cua ban la:",d)
elif a<=8:
    d=3*13000+(a-3)*12000
    print("so tien cua ban la:",d)
elif a>8:
    d=3*13000+4*12000+(a-7)*10000
    if d>100000:
        d=d-d*0.08
        print("tien ban duoc giam 8%,so tien cua ban la",d)
    else:
        print("so tien cua ban la:",d)

    