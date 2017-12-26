---
layout: post
categories: [python]
title: python数据库操作pymysql
date: 2016-08-30
author: TTyb
desc: "python数据库操作pymysql"
---

安装数据库：

~~~ruby
pip3 install pymysql
~~~

进行数据库的更新、插入、查询等操作：

~~~ruby
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#-----------------原表格-----------------

#+-------+-----------+------------+------+
#| mid   | name      | birth      | sex  |
#+-------+-----------+------------+------+
#| G0001 | 杜意意    | 1975-04-18 | 0    |
#| G0002 | 李玉      | NULL       | 1    |
#| H0001 | 李加      | NULL       | 0    |
#| N0001 | 小小      | 1980-11-23 | 1    |
#+-------+-----------+------------+------+

import pymysql

# 连接数据库
mysql = pymysql.connect(host="localhost", user="root", passwd="1111", db="test", charset="utf8")

# 获取操作游标
cur = mysql.cursor()

# 查找
lookup = input('请输入查找语句：')
# 将查找语句放入操作中
# 执行成功后sta值为1
sta = cur.execute(lookup)
# 打印出查找的东西
# 这里也可以编码item[].decode('UTF-8')
for item in cur:
    print("Id=" + str(item[0]) + " name=" + str(item[1]) + " birth=" + str(item[2]) + " sex=" + str(item[3]))

# 插入、更新
# 插入王五
# insert into customer(mid,name,birth,sex) values('G0001','王五','1992-01-03','1');
# 将G0002名字改为李玉枝，生日补齐
# update customer set name='李玉枝',birth='1980-09-09' where mid='G0002';
insert = input('请输入插入(更新)语句：')
# 将查找语句放入操作中
# 执行成功后sta值为1
sta = cur.execute(insert)
# 最后确定后下面语句将真正插入进去
# 如果只是测试代码对不对可以将其注释掉
mysql.commit()

# 关闭操作游标
cur.close()

# 关闭数据库
mysql.close()
~~~