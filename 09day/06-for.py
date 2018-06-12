#!/usr/bin/env python
# coding=utf-8
a = 0
b = 0
for i in range(0,101):
    if i%2==0:
        print("偶数是%d"%i)
        a += i
    else:
        print("奇数是%d"%i)
        b += i
print("偶数和是%d"%a)
print("奇数和是%d"%b)
