#!/usr/bin/env python
# coding=utf-8
list_1=[]
while True:
    list_2=[]
    list_1.append(list_2)
    people=int(input("请选择您要操作的选项\n1--添加商品\n2--删除商品\n3--修改商品\n4--退出"))
    if people==1:
        add1=input("请输入您要添加的商品： ")
        list_2.append(add1)
        add2=input("请输入商品的价格： ")
        list_2.append(add2)
        print(list_1)
    elif people==2:
        shan=input("请输入你要删除的商品： ")
        for i in list_1:
            print(i)
            if shan in i[0]:
                print(shan)

        #else:
            #print("没有此商品")
