#!usr/bin/env python3
# -*- coding:utf-8 -*-

a = 19
b = 18

if a > 18:
    print("ok,成年人")
elif a == 18:
    print("刚好18岁")
else:
    print("不ok,未成年人")

if b > 18:
    print("ok,成年人")
elif b == 18:
    print("刚刚好18岁")
else:
    print("不ok,未成年人")

if a > 18 and b > 18:
    print("都过了18")
elif a > 18 or b > 18:
    print("有一个过了18")
else:
    print("滚犊子")

