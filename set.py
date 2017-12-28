#!usr/bin/env python3
# -*- coding:utf-8 -*-

set1 = set([123, 456, 678])
set1.add(100)
print(set1)
set1.add(100)
print(set1)


# 交集 并集 差集
set2 = set('hello')
set3 = set(['a', 'c', 'e', 'l', '1'])
set4 = set2 & set3
print(set4)
set5 = set2 | set3
print(set5)

set6 = set2 - set3
set7 = set3 - set2
print(set6)
print(set7)


# 数组去重  贼好用
list1 = [1, 2, 1, 3, 1, 3, 2, 4, 1, 55, 3, 2]
set1 = set(list1)
print(set1)
