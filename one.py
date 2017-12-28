#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    learing python
    basic...
"""

a = "hello world"
print("hello world")
print(a)
print(None)

TEST_STR = "12"

b = int(TEST_STR)
print(b)

# c = long(TEST_STR)
# print(c)

d = float(TEST_STR)
print(d)

list1 = ["1", "二", 3]
print(list1[1])
list1.append("4")
print(list1)

del list1[1]
print(list1)

print(len(list1))
