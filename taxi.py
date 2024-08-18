# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:00:48 2024

@author: Student
"""
a = "tiền taxi"
x = float(input("Nhập số km quãng đường đi được: "))
if x >= 1 and x < 3:
    a = 20*x
    print("số tiền taxi là", a)
elif x >= 3 and x < 4:
    a = 13*x
    print("số tiền taxi là", a)
elif x >=4 and x < 8:
    a = 12*x
    print("số tiền taxi là", a)
elif x > 100:
    a = 10*x - 8/100*10*x
    print("số tiền taxi là", a)
else:
    a = 10*x
    print("số tiền taxi là", a)

    
    