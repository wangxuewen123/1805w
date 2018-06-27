#!/usr/bin/env python
# coding=utf-8
#声明函数
def sa(year,month,day):
    month_big = [1,3,5,7,8,10,12]#定义大月的列表
    month_small = [4,6,9,11]#定义小月的列表，2月比较特殊不加进去
    zong_day = 0#定义保存总天数的变量
    for i in range(1,month):#遍历月份
        #如果月份在大月里面就加31天
        if i in month_big:
            zong_day += 31
        #如果月份在小月里面就加30天
        if i in month_small:
            zong_day += 30
        #如果月份是2月就判断润还是平
        if i == 2:
            if (year%4 == 0 and year%100 != 0) or year%400 == 0:#判断这个二月润年月还是平年月
                zong_day += 29
            else:
                zong_day += 28
    zong_day += day#必须加上当前月的天数
    print("%d年有%d天"%(year,zong_day))
#调用函数
years = int(input("请输入年： "))
months = int(input("请输入月： "))
days = int(input("请输入天： "))
sa(years,months,days)
