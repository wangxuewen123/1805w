#!/usr/bin/env python
# coding=utf-8
'''
name = "小明"
print("我的名字是%s"%name)
student_no = 1
print("我的学好是%06d"%student_no)
price = 7.5
weight = 15
money = price*weight
print("西瓜的单价是%.2f元\n重量是%d斤\n宁需要支付%.2f元"%(price,weight,money))
scale = 3.4
print("数据比例是%.2f%%"%(scale * 100))
'''
#定义变量
a = int(input("请输入一年有多少天： "))#输入一年的天数
b = a*24#时
c = b*60#分
d = c*60#秒
print("一年有%d天\n一年有%d小时\n一年有%d分\n一年有%d秒"%(a,b,c,d))

