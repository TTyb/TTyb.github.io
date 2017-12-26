---
layout: post
categories: [scala]
title: scala中spark运行内存不足
date: 2017-04-18
author: TTyb
desc: "scala中spark运行内存不足"
---

用 `bash spark-submit` 在spark上跑代码的时候出现错误：

~~~ruby
ERROR executor.Executor: Exception in task 9.0 in stage 416.0 (TID 18363)
java.lang.OutOfMemoryError: Java heap space
~~~

发现其原因竟然是运行的时候默认的内存不足以支撑海量数据，可以用 `bash spark-submit --help` 中查看到自己代码的运行内存，即：

~~~ruby
--driver-memory MEM         Memory for driver (e.g. 1000M, 2G) (Default: 1024M)
~~~

本机默认为1G的内存运行程序，所以我改成8G内存运行：

~~~ruby
bash spark-submit --driver-memory 8G --class MF字段 你的jar名字.jar
~~~

具体运行请看：

[scala打包jar并在Linux下运行](https://ttyb.github.io/scala/scala%E6%89%93%E5%8C%85jar%E5%B9%B6%E5%9C%A8Linux%E4%B8%8B%E8%BF%90%E8%A1%8C.html)

查看 `Linux` 的内存命令为：

`cat /proc/meminfo |grep MemTotal`

