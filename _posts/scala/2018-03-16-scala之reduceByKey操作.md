---
layout: post
categories: [scala]
title: scala之reduceByKey操作
date: 2018-03-16
author: TTyb
desc: "需要对dataframe按照某几列为key，对另外几列进行计算，考虑到scala的reduceByKey比groupByKey快速很多，所以使用了这个操作"
---

原始 `dataFrame` ：

~~~ruby
val dataFrame = spark.createDataFrame(Seq(
  ("l12", 2, "col1"),
  ("l13", 3, "col2"),
  ("l13", 32, "col2"),
  ("l13", 35, "col3"),
  ("l14", 4, "col4")
)).toDF("label", "num", "col")
dataFrame.show(false)
+-----+---+----+
|label|num|col |
+-----+---+----+
|l12  |2  |col1|
|l13  |3  |col2|
|l13  |32 |col2|
|l13  |35 |col3|
|l14  |4  |col4|
+-----+---+----+
~~~

需要选出相同的 `label` 下，`num` 最大的一个，也就是要过滤掉 `label=l13,num=3` 和 `label=l13,num=32`。

计算以 `label` 为 `key` ，比较相同的 `label` 下，`num` 最大的一个，这里确定 `key` 用 `keyBy`：

~~~ruby
val resultDataframe = dataFrame.rdd.map {
  line =>
	(line.getAs[String]("label"), line.getAs[Int]("num"), line.getAs[String]("col"))
}.keyBy(_._1).reduceByKey {
  (ele1, ele2) =>
	val result = if (ele1._2 > ele2._2)
	  ele1
	else
	  ele2
	result
}.map(_._2).toDF("label", "num", "col")
~~~

得到结果为：

~~~ruby
+-----+---+----+
|label|num|col |
+-----+---+----+
|l14  |4  |col4|
|l12  |2  |col1|
|l13  |35 |col3|
+-----+---+----+
~~~

但是如果存在多个 `key` ，上面的方法只是一个 `key` 的写法，假设要以 `label` 和 `col` 为 `key` ，那么将会过滤掉 `label=l13,num=3,col=col2`，代码如下：

~~~ruby
val resultDataframe = dataFrame.rdd.map {
  line =>
	(line.getAs[String]("label"), line.getAs[Int]("num"), line.getAs[String]("col"))
}.keyBy(each => (each._1, each._3)).reduceByKey {
  (ele1, ele2) =>
	val result = if (ele1._2 > ele2._2)
	  ele1
	else
	  ele2
	result
}.map(_._2).toDF("label", "num", "col")
resultDataframe.show(false)
~~~

得到结果为：

~~~ruby
+-----+---+----+
|label|num|col |
+-----+---+----+
|l12  |2  |col1|
|l13  |32 |col2|
|l14  |4  |col4|
|l13  |35 |col3|
+-----+---+----+
~~~