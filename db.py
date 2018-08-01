#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user="root",password="123456qq0.0AA",database="test",use_unicode=True)

cursor = conn.cursor()

#创建表
#cursor.execute("create table user (id varchar(20) primary key ,name varchar(20))")
cursor.execute("insert into user (id,name) values (%s,%s)",["1","panghu"])
cursor.rowcount
1
#提交事务
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute("select * from user")
values = cursor.fetchall()

print (values)
cursor.close()
conn.close()












