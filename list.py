#!usr/bin/env python3
# -*- coding:utf-8 -*-

# ------------------------ list ------------------------

# 1. 如果一个产品，需要列出产品的用户，这时候就可以使用一个 list 来表示
users = ["老王", "老张", "老李"]
print("1.用户以下这些")
print(users)

# 2.统计用户有多少人
print("\n2.用户有多少人")
print(len(users))

# 3.具体的用户有谁
print("\n3.具体的是谁")
print(users[0]+','+users[1]+","+users[2])

# 4.新增一个用户
users.append("老马")
print("\n4.新增一个用户")
print(users)

# 5.插入用户 insert
users.insert(0, "VIP用户")
print("\n5.插入VIP用户")
print(users)

# 6.删除老马
users.pop()
print("\n6.删除最后一个用户")
print(users)
 
# 7.删除制定位置用户
users.pop(1)
print("\n7.删除指定位置用户")
print(users)

# 8.修改List某一用户名
users[1] = "王老人家"
print("\n8修改某一用户名")
print(users)

# 9.添加金额
newUsers = [["老王", 123], ["老李", 456]]
print("\n9.不同类型元素")
print(newUsers)
