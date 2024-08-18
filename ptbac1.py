# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:40:55 2024

@author: Student
"""
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
else:
    print("Nghiệm của phương trình là x = ", -b / a)

    
    

