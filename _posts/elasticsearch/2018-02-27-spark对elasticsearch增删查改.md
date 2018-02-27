---
layout: post
categories: [elasticsearch]
title: spark对elasticsearch增删查改
date: 2018-02-27
author: TTyb
desc: "spark调用elsticsearch的API对elasticsearch进行增删查改"
---


### 增

新建一个 `dataframe` ，插入到索引 `_index/_type` ，直接调用 `saveToEs` ，让 `_id` 为自己设定的 `id`：

~~~ruby
import org.elasticsearch.spark.sql._
def main(args: Array[String]): Unit = {

val spark = getSparkSession()
val dataFrame = spark.createDataFrame(Seq(
  (1, 1, "2", "5"),
  (2, 2, "3", "6"),
  (3, 2, "36", "69")
)).toDF("id", "label", "col1", "col2")
dataFrame.saveToEs("_index/_type",Map("es.mapping.id" -> "id"))
}

//配置spark
def getSparkSession(): SparkSession = {
val masterUrl = "local"
val appName = "ttyb"
val sparkconf = new SparkConf()
  .setMaster(masterUrl)
  .setAppName(appName)
  .set("es.nodes", "es的IP")
  .set("es.port", "9200")
val Spark = SparkSession.builder().config(sparkconf).getOrCreate()
Spark
}
~~~

### 删

目前 `spark` 没有开放删除的 `API` ，所以删除只能用命令行：

~~~ruby
curl -XDELETE 'http://es的IP:9200/_index/_type/_id'
~~~

### 查

根据时间范围查询，其中 `query` 可以为空，代表不以任何查询条件查询：

~~~ruby
val startTime = "1519660800000"
val endTime = "1519747200000"
val query = "{\"query\":{\"range\":{\"recordtime\":{\"gte\":" + startTime + ",\"lte\":" + endTime + "}}}}"
val tableName = "_index/_type"
val botResultData = spark.esDF(tableName, query)
~~~

### 改

例如需要将 `id=3` 的 `col1` 改成 `4` ，`col2` 改成 `7`，可以新建一个 `dataframe` ，按照 `id` 储存，这样 `elasticsearch` 就会自动覆盖相同 `id` 下的数据：

~~~ruby
val dataFrame1 = spark.createDataFrame(Seq(
  (3, 2, "4", "7")
)).toDF("id", "label", "col1", "col2")
dataFrame1.saveToEs("_index/_type",Map("es.mapping.id" -> "id"))
~~~