#!/usr/bin/env python
# coding=utf-8
a = 1
d = 0
while a <= 10:
    b = 0
    while b < 2:
        c = 0
        while c < 1:
            c+=1
        b+=1
    d = a*b*c
    a+=1
print(d)
