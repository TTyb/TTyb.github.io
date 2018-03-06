---
layout: post
categories: [scala]
title: 将Spark Dataframe转换为Scala Map集合
date: 2018-03-06
author: TTyb
desc: "需要将Spark Dataframe转换为Scala Map集合"
---

原始 `dataFrame` ：

~~~ruby
df.show
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+
~~~

方式一 ：

~~~ruby
val peopleArray = df.collect.map(r => Map(df.columns.zip(r.toSeq):_*))
~~~

得到结果：

~~~ruby
Array(
  Map("age" -> null, "name" -> "Michael"),
  Map("age" -> 30, "name" -> "Andy"),
  Map("age" -> 19, "name" -> "Justin")
)
~~~

方式二 ：

~~~ruby
val people = Map(peopleArray.map(p => (p.getOrElse("name", null), p)):_*)
~~~

得到结果：

~~~ruby
Map(
  ("Michael" -> Map("age" -> null, "name" -> "Michael")),
  ("Andy" -> Map("age" -> 30, "name" -> "Andy")),
  ("Justin" -> Map("age" -> 19, "name" -> "Justin"))
)
~~~

方式三 ：

~~~ruby
val indexedPeople = Map(peopleArray.zipWithIndex.map(r => (r._2, r._1)):_*)
~~~

得到结果：

~~~ruby
Map(
  (0 -> Map("age" -> null, "name" -> "Michael")),
  (1 -> Map("age" -> 30, "name" -> "Andy")),
  (2 -> Map("age" -> 19, "name" -> "Justin"))
)
~~~