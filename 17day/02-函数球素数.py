#!/usr/bin/env python
# coding=utf-8
def aa():
    lista = []
    for i in range(2,101):
        falg = 0
        for a in range(2,i-1):
            if i%a == 0:
                falg = 1
                print(i)
                break
        if falg == 0:
            lista.append(i)
    return lista
rulse = aa()
print(rulse)
