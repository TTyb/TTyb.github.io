---
layout: post
categories: [hadoop]
title: hadoop退出安全模式Name node is in safe mode
date: 2018-01-12
author: TTyb
desc: "hadoop使用出现安全模式错误Name node is in safe mode，退出安全模式"
---

在使用 `hdfs` 的时候出现如下错误：

~~~ruby
18/01/12 09:04:34 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 0 minutes, Emptier interval = 0 minutes.
rm: Cannot delete /spark/data/netflow/201801120325.txt. Name node is in safe mode.
~~~

`hadoop` 处于安全模式，所以需要退出安全模式，一般以如下方法可以解决：

~~~ruby
hadoop dfsadmin -safemode leave
~~~

实在不行还可以用如下方式：

~~~ruby
hdfs dfsadmin -safemode leave
~~~