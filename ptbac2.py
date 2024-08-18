# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:01:46 2024

@author: Student
"""
import math
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))
delta = b**2 - 4*a*c
if delta == 0:
     x1 = x2 = -b / (2*a)
     print("Phương trình có nghiệm kép", x1 = x2)
elif delta >= 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("phương trình có 2 nghiệm phân biệt:", x1,"và", x2)
else:
    print("Phương trình vô nghiệm")   
    
    
    
    
    
