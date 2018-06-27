#!/usr/bin/env python
# coding=utf-8
def jie(number):
    if number == 1:
        return 1
    else:
        return number*jie(number-1)
res = jie(700)
print(res)
