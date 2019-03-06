---
layout: post
categories: [scala]
title: DataFrameNaFunctions无fill方法
date: 2019-03-06
author: TTyb
desc: "java.lang.NoSuchMethodError: org.apache.spark.sql.DataFrameNaFunctions.fill(JLscala/collection/Seq;)Lorg/apache/spark/sql/Dataset"
---

当我使用 `spark2.1` ，为了填补 `dataframe` 里面的 `null` 值转换为 `0` ，代码如下所示：

~~~ruby
dataframe.na.fill(0)
~~~

出现如下错误 `Spark version 2.1.0 returns following error` :

~~~ruby
java.lang.NoSuchMethodError: org.apache.spark.sql.DataFrameNaFunctions.fill(JLscala/collection/Seq;)Lorg/apache/spark/sql/Dataset
~~~

原来在 `spark2.1` 版本暂时不支持 `na.fill` 写法，因此查询众多方式得到解决：

~~~ruby
import org.apache.spark.sql.functions.when
val dataDF = dataframe.withColumn("col", when(dataframe("col").isNull,0).otherwise(dataframe("col")))
~~~

