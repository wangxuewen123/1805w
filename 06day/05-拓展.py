#!/usr/bin/env python
# coding=utf-8
#ATM取款机系统
account = input("请输入您的账号  ")
passwd = input("请输入密码  ")
name = input("请输入姓名  ")
money = float(input("您要春的钱  "))
qu = float(input("您要取得钱  "))
yu = money-qu
print("="*50)
print("姓名  %s\n帐号  %s\n密码  %s\n卡上金额  %.2f元\n本次要取  %.2f元\n余额  %.2f元"%(name,account,passwd,money,qu,yu))
print("="*50)
