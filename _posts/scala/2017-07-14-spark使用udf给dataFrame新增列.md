---
layout: post
categories: [scala]
title: spark使用udf给dataFrame新增列
date: 2017-07-14
author: TTyb
desc: "在spark中给dataframe增加一列的方法一般使用withColumn，但是个人感觉少了很多功能，不如使用udf"
---

在 `spark` 中给 `dataframe` 增加一列的方法一般使用 `withColumn`

```
// 新建一个dataFrame
val sparkconf = new SparkConf()
  .setMaster("local")
  .setAppName("test")
val spark = SparkSession.builder().config(sparkconf).getOrCreate()
val tempDataFrame = spark.createDataFrame(Seq(
  (1, "asf"),
  (2, "2143"),
  (3, "rfds")
)).toDF("id", "content")
// 增加一列
val addColDataframe = tempDataFrame.withColumn("col", tempDataFrame("id")*0)
addColDataframe.show(10,false)
```

打印结果如下：

```
+---+-------+---+
|id |content|col|
+---+-------+---+
|1  |asf    |0  |
|2  |2143   |0  |
|3  |rfds   |0  |
+---+-------+---+
```

可以看到 `withColumn` 很依赖原来 `dataFrame` 的结构，但是假设没有 `id` 这一列，那么增加列的时候灵活度就降低了很多，假设原始 `dataFrame` 如下：

```
+---+-------+
| id|content|
+---+-------+
|  a|    asf|
|  b|   2143|
|  b|   rfds|
+---+-------+
```

这样可以用 `udf` 写自定义函数进行增加列：

```
import org.apache.spark.sql.functions.udf
// 新建一个dataFrame
val sparkconf = new SparkConf()
  .setMaster("local")
  .setAppName("test")
val spark = SparkSession.builder().config(sparkconf).getOrCreate()
val tempDataFrame = spark.createDataFrame(Seq(
  ("a, "asf"),
  ("b, "2143"),
  ("c, "rfds")
)).toDF("id", "content")
// 自定义udf的函数
val code = (arg: String) => {
      if (arg.getClass.getName == "java.lang.String") 1 else 0
    }

val addCol = udf(code)
// 增加一列
val addColDataframe = tempDataFrame.withColumn("col", addCol(tempDataFrame("id")))
addColDataframe.show(10, false)
```

得到结果：

```
+---+-------+---+
|id |content|col|
+---+-------+---+
|a  |asf    |1  |
|b  |2143   |1  |
|c  |rfds   |1  |
+---+-------+---+
```

还可以写下更多的逻辑判断：

```
// 新建一个dataFrame
val sparkconf = new SparkConf()
  .setMaster("local")
  .setAppName("test")
val spark = SparkSession.builder().config(sparkconf).getOrCreate()
val tempDataFrame = spark.createDataFrame(Seq(
  (1, "asf"),
  (2, "2143"),
  (3, "rfds")
)).toDF("id", "content")

val code :(Int => String) = (arg: Int) => {if (arg < 2) "little" else "big"}
val addCol = udf(code)
val addColDataframe = tempDataFrame.withColumn("col", addCol(tempDataFrame("id")))
addColDataframe.show(10, false)
```

```
+---+-------+------+
|1  |asf    |little|
|2  |2143   |big   |
|3  |rfds   |big   |
+---+-------+------+
```

传入多个参数：

```
val sparkconf = new SparkConf()
  .setMaster("local")
  .setAppName("test")
val spark = SparkSession.builder().config(sparkconf).getOrCreate()
val tempDataFrame = spark.createDataFrame(Seq(
  ("1", "2"),
  ("2", "3"),
  ("3", "1")
)).toDF("content1", "content2")

val code = (arg1: String, arg2: String) => {
  Try(if (arg1.toInt > arg2.toInt) "arg1>arg2" else "arg1<=arg2").getOrElse("error")
}
val compareUdf = udf(code)

val addColDataframe = tempDataFrame.withColumn("compare", compareUdf(tempDataFrame("content1"),tempDataFrame("content2")))
addColDataframe.show(10, false)
```

```
+--------+--------+----------+
|content1|content2|compare   |
+--------+--------+----------+
|1       |2       |arg1<=arg2|
|2       |3       |arg1<=arg2|
|3       |1       |arg1>arg2 |
+--------+--------+----------+
```