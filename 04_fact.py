# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:00:32 2024

@author: User
"""

n = int(input("정수를 입력하시오 : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    
print(f"{n}!은 {fact}이다.")