# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:42:54 2024

@author: Student
"""

a = float(input("Nhập cạnh a:"))
b = float(input("Nhập cạnh b:"))
c = float(input("Nhập cạnh c:"))
if a**2 == b*c or b**2 == a*c or c**2 == a*b:
    print("Tam giác này là tam giác vuông")
elif a == b == c:
    print("Tam giác này là tam giác đều")
elif a == b or a == c or b == c:
    print("Tam giác này là tam giác cân")
else:
    print("Tam giác này là tam giác thường")
    
    