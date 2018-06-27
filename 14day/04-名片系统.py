#!/usr/bin/env python
# coding=utf-8
lista = []
while True:
    print("欢迎进入名片系统".center(50,"*"))
    print("1-添加名片".center(50," "))
    print("2-查询名片".center(50," "))
    print("3-修改名片".center(50," "))
    print("4-删除名片".center(50," "))
    print("5-查看名片".center(50," "))
    print("6-退出系统".center(50," "))
    me = input("请输入您要操作的选项： ")
    #添加
    dic = {}
    if me == "1":
        print("添加名片".center(50,"="))
        a = input("请输入姓名： ")
        b = input("请输入年龄： ")
        c = input("请输入性别： ")
        d = input("请输入电话： ")
        e = input("请输入公司： ")
        dic1 = {"name":a,
                "age":b,
                "sex":c,
                "phone":d,
                "gongsi":e}
        dic.update(dic1)#把输入的名片添加到总列表里面
        lista.append(dic1)#把输入的内容添加到上面的字典里面
        print("添加成功".center(50,"^"))
        #下面是让字典中的内容更加人性化显示
        for a,b in dic.items():
            print(a,b)
    #查询=================================================================================
    elif me == "2":
        print("查询名片".center(50,"="))
        cha = input("请输入姓名： ")
        for i in lista:#遍历一下大列表
            if cha == i["name"]:#如果输入的内容等于i字典的value
                print("姓名 %s"%i["name"])
                print("年龄 %s"%i["age"])
                print("性别 %s"%i["sex"])
                print("电话 %s"%i["phone"])
                print("公司 %s"%i["gongsi"])
                break
        else:
            print("没有这个名片～～xie")
    #修改=================================================================================
    elif me == "3":
        print("修改名片".center(50,"="))
        gai = input("你要修改谁的名片：  ")
        for i in lista:#遍历大列表
            if gai == i["name"]:#如果你输入的内容有的话，往下执行
                print("1.修改姓名\n2.修改年龄\n3.修改性别\n4.修改电话\n5.修改公司")
                a = int(input("请输入选项： "))
                if a == 1:
                    b = input("请输入新的姓名： ")
                    i["name"] = b
                    print("修改成功新的姓名为 %s"%i["name"])
                elif a == 2:
                    n = input("请输入新的年龄： ")
                    i["age"] = n
                    print("修改成功新的年龄为 %s"%i["age"])
                elif a == 3:
                    sex = input("请输入新的性别： ")
                    i["sex"] = sex
                elif a == 4:
                    phone = input("请输入新的电话： ")
                    i["phone"] = phone
                    print("修改成功新的电话为 %s"%i["phone"])
                elif a == 5:
                    comply = input("请输入新的公司名称: ")
                    i["gongsi"] = comply
                    print("修改成功新的公司名称为 %s"%i["gongsi"])
                break
        else:
            print("没有这个名片～～～～～～")
    #删除=============================================================================
    elif me == "4":
        print("删除名片".center(50,"="))
        shan = input("请输入你要删除的名片： ")
        for a,i in enumerate(lista):
            if shan == i["name"]:
                lista.pop(a)
                print("删除成功")
                break
        else:
            print("没有这个名片")
    #查看名片=========================================================================
    elif me == "5":
        print("查看名片".center(50,"="))
        a = 0
        for i in lista:
            if len(lista) >= 1:
                a = 1
                print("姓名 %s\n年龄 %s\n性别 %s\n公司 %s\n电话 %s\n>>>>>>>>>>>>>>>"%(i["name"],i["age"],i["sex"],i["gongsi"],i["phone"]))
        if a == 0:
            print("没有了")
    #退出=============================================================================
    elif me == "6":
        print("欢迎下次再来".center(50,"="))
        break
    else:
        print("请输入错误")
