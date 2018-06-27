---
layout: post
categories: [scala]
title: dataframe行变换为列
date: 2018-06-27
author: TTyb
desc: "需要将dataframe中的某一行变换为列"
---

新建一个 `dataFrame` ：

~~~ruby
val conf = new SparkConf().setAppName("TTyb").setMaster("local")
val sc = new SparkContext(conf)
val spark: SQLContext = new SQLContext(sc)
import org.apache.spark.sql.functions.explode
import org.apache.spark.sql.functions.split
import spark.implicits._
val dataFrame = spark.createDataFrame(Seq(
  (1, "example1", "a|b|c"),
  (2, "example2", "d|e")
)).toDF("id", "name", "content")
~~~

需要将 `content` 的内容按照 `|` 分割，得到如下效果：

~~~ruby
+---+--------+-------+
| id|    name|content|
+---+--------+-------+
|  1|example1|      a|
|  1|example1|      b|
|  1|example1|      c|
|  2|example2|      d|
|  2|example2|      e|
+---+--------+-------+
~~~

目前有两种方式实现。

### 方式一

使用 `import org.apache.spark.sql.functions` 里面的函数，具体的方式可以看 [functions](http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$) ：

~~~ruby
import org.apache.spark.sql.functions.{explode,split}
import spark.implicits._
dataFrame.withColumn("content", explode(split($"content", "[|]"))).show
```

### 方式二

使用 `udf` ，具体的方式可以看 [spark使用udf给dataFrame新增列](http://www.tybai.com/scala/spark%E4%BD%BF%E7%94%A8udf%E7%BB%99dataFrame%E6%96%B0%E5%A2%9E%E5%88%97.html)

~~~ruby
import org.apache.spark.sql.functions.explode
val stringtoArray =org.apache.spark.sql.functions.udf((content : String) => {content.split('|')})
dataFrame.withColumn("content", explode(stringtoArray(dataFrame("content")))).show
```

