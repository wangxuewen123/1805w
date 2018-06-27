#!/usr/bin/env python
# coding=utf-8
lista = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
for i in lista:
    print(i)
    for b,c in i.items():
        print(b,c)
        for d,f in c.items():
            print(b,d,f)
