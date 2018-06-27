#!/usr/bin/env python
# coding=utf-8
list_a = []#装注册的账号和密码
def zhuce():
    account = input("请输入帐号(11位数的数字)： ")
    passwd = input("请输入密码(6位数以上的密码)： ")
    dic1 = {"account":account,
            "passwd":passwd}
    list_a.append(dic1)
    for i in list_a:
        print("帐号： %s"%i["account"])
        print("密码： %s"%i["passwd"])
    if len(account) == 11 and account.startswith("1") and len(passwd) > 6:
        print("注册成功")
    else:
        print("注册失败")
zhuce()
def loing(account,passwd):
    for i in list_a:
        if account == i["account"] and passwd == i["passwd"]:
            print("登录成功")
        else:
            print("登陆失败")
if list_a:
    acc = input("请输入帐号： ")
    pwd = input("请输入密码： ")
    loing(acc,pwd)
