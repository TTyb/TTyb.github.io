---
layout: post
categories: [elasticsearch]
title: spark Could not write all entries
date: 2018-03-01
author: TTyb
desc: "Caused by: org.elasticsearch.hadoop.EsHadoopException: Could not write all entries [1/1] (Maybe ES was overloaded?). Error sample..."
---


使用 `spark` 将 `dataFrame` 储存到 `elasticsearch` 出现如下报错：

~~~ruby
Caused by: org.elasticsearch.hadoop.EsHadoopException: Could not write all entries [1/1] (Maybe ES was overloaded?). Error sample (first [1] error messages):
	rejected execution of org.elasticsearch.transport.TransportService$4@7d5f91de on EsThreadPoolExecutor[bulk, queue capacity = 50, org.elasticsearch.common.util.concurrent.EsThreadPoolExecutor@3447703a[Running, pool size = 32, active threads = 32, queued tasks = 68, completed tasks = 9151096]]
Bailing out...
~~~

这个无法查到定位到报错位置，所以在新建 `spark` 的时候进行如下配置：

~~~ruby
val masterUrl = "local"
val appName = "ttyb"
val sparkConf = new SparkConf()
  .setMaster(masterUrl)
  .setAppName(appName)
  .set("es.nodes", "172.16.14.21")
  .set("es.port", "9200")
  //Bailing out...错误
  .set("es.batch.size.entries", "1")
  //插入失败后无限重复插数据
  .set("es.batch.write.retry.count", "-1")
  //查数据等待时间
  .set("es.batch.write.retry.wait", "100")
val Spark = SparkSession.builder().config(sparkConf).getOrCreate()
~~~

得到新的错误：

~~~ruby
org.elasticsearch.hadoop.rest.EsHadoopInvalidRequest: 
null
~~~

报错显示： 

> `ES` 负载过高，需要重新修复

本想重启 `ES` ，发现是机器 `磁盘空间已满` ，查错成功

