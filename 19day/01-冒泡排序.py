#!/usr/bin/env python
# coding=utf-8
lista = [12,3,4,122,6,45,8,5]
for i in range(0,len(lista)-1):
    for a in range(i+1,len(lista)):
        if lista[i] > lista[a]:
            lista[i],lista[a] = lista[a],lista[i]
    print(lista)
