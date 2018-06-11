#!/usr/bin/env python
# coding=utf-8
#第一题
weizhi = input("请输入你的站位===>  ")
if weizhi == "ADC":
    print("后裔 黄总 虞姬")
elif weizhi == "坦克":
    print("亚瑟 程咬金")
elif weizhi == "法师":
    print("王昭君 妲姬")
elif weizhi == "刺客":
    print("蓝领王 阿克")
else:
    print("没有这个位置")
#第二题
print("============================分割===============================")
year = int(input("请输入年份： "))
if year%4 == 0 and year%100 != 0:
    print("润年")
elif year%400 == 0:
    print("也是润年")
else:
    print("不是润年")
print("============================分割==============================")
#第三题

