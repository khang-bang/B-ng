# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:33:01 2024

@author: Student
"""

a = float(input("Nhập cạnh a:"))
b = float(input("Nhập cạnh b:"))
c = float(input("Nhập cạnh c:"))
if a + b > c and b + c > a and a + c >b:
            print("a, b,c là cạnh của tam giác")
else:
    print("a, b,c không là cạnh của tam giác")
    