# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:38:50 2024

@author: Student
"""

ĐTB = float(input("Nhập điểm trung bình (GPA):"))
if ĐTB >= 3.5 and ĐTB < 5.0:
    print("Học lực yếu")
elif ĐTB >= 5.0 and ĐTB < 7:
    print("Học lực trung bình")
elif ĐTB >= 7.0 and ĐTB < 8.0:
    print("Học lực khá")
elif ĐTB >= 8.0 and ĐTB < 9.0:
    print("Học lực giỏi")
elif ĐTB >= 9.0 and ĐTB <= 10:
    print("Học lực xuất sắc")
else:
    print("Học lực kém")