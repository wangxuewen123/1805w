#!/usr/bin/env python
# coding=utf-8
account = 1234
passwd = 12345
user = int(input("请输入用户名： "))
mima = int(input("请输入密码： "))
if user == account and mima == passwd:
    print("欢迎进入我的世界")
else:
    print("密码或用户错误")
