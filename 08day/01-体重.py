#!/usr/bin/env python
# coding=utf-8
height = float(input("请输入身高(m)： "))
weight = float(input("请输入体重(kg)： "))
bmi = weight/height ** 2
print("您的bmi指数为%.2f"%bmi)
if bmi < 18.5:
    print("过轻")
elif bmi < 18.5 and bmi > 25:
    print("正常")
elif bmi < 25 and bmi > 28:
    print("过重")
elif bmi < 28 and bmi > 32:
    print("肥胖")
elif bmi > 32:
    print("严重肥胖")
