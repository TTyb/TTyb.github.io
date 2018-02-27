---
layout: post
categories: [scala]
title: spark按某几列删除dataframe重复行
date: 2018-02-27
author: TTyb
desc: "spark调用distinct只能删除完全相同的行，而需要一种方法按照某几列作为唯一ID来删除重复，利用dropDuplicates可以完美解决这个问题"
---

新建一个 `dataframe` ：

~~~ruby
val conf = new SparkConf().setAppName("TTyb").setMaster("local")
val sc = new SparkContext(conf)
val spark = new SQLContext(sc)
val dataFrame = spark.createDataFrame(Seq(
  (1, 1, "2", "5"),
  (2, 2, "3", "6"),
  (2, 2, "35", "68"),
  (2, 2, "34", "67"),
  (2, 2, "38", "68"),
  (3, 2, "36", "69"),
  (1, 3, "4", null)
)).toDF("id", "label", "col1", "col2")
~~~

想根据 `id` 和 `lable` 来删除重复行，即删掉 `id=2` 且 `lable=2` 的重复行。利用 `distinct` 无法删除

~~~ruby
dataframe.distinct().show()
+---+-----+----+----+
| id|label|col1|col2|
+---+-----+----+----+
|  1|    1|   2|   5|
|  2|    2|   3|   6|
|  2|    2|  35|  68|
|  2|    2|  34|  67|
|  2|    2|  38|  68|
|  3|    2|  36|  69|
|  1|    3|   4|null|
+---+-----+----+----+
~~~

利用 `dropDuplicates` 可以根据 `ID` 来删除：

~~~ruby
dataFrame.dropDuplicates("id","label").show()
+---+-----+----+----+
| id|label|col1|col2|
+---+-----+----+----+
|  2|    2|   3|   6|
|  1|    1|   2|   5|
|  1|    3|   4|null|
|  3|    2|  36|  69|
+---+-----+----+----+
~~~