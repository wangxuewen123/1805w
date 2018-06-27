#!/usr/bin/env python
# coding=utf-8
a=int({"a":2,"b":3})
for i in a.items():
    print(i["a"])
    print(i["b"])
    print(type(i["a"]))
    print(type(i["b"]))
