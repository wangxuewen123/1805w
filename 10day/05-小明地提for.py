#!/usr/bin/env python
# coding=utf-8
import random
all_money = 0#消费总钱数

for i in range(1,31):#每月30天
    for j in range(1,3):#每天2次
        km = random.randint(1,100)
        if km <= 6:
            price = 3
        elif km > 6 and km <= 12:
            price = 4
        elif km >12 and km <= 22:
            price = 5
        elif km > 22 and km <= 32:
            price = 6
        elif km > 32:
            if (km-32)%20 == 0:
                price = 6+(km-32)/20
            else:
                price = 6+int((km-32)/20)+1
        all_money = all_money + price
if all_money >= 100 and all_money < 150:
    print(((all_money-100)*0.8)+100)
elif all_money >= 150 and all_money < 400:
    print(((all_money-150)*0.5)+150)
print("总钱%.2f"%all_money)
    
