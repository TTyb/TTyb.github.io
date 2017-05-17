---
layout: post
categories: [scala]
title: scala的reduce
date: 2017-05-17
author: TTyb
desc: "`spark` 中的 `reduce` 非常的好用，`reduce` 可以对 `dataframe` 中的元素进行计算、拼接等等"
---

`spark` 中的 `reduce` 非常的好用，`reduce` 可以对 `dataframe` 中的元素进行计算、拼接等等。例如生成了一个 `dataframe` :

```
//配置spark
  def getSparkSession(): SparkSession = {

    //读取配置文件
    val properties: Properties = new Properties()
    val ipstream: InputStream = this.getClass().getResourceAsStream("/config.properties")
    properties.load(ipstream)

    val masterUrl = properties.getProperty("spark.master.url")
    val appName = properties.getProperty("spark.app.name")
    val sparkconf = new SparkConf()
      .setMaster(masterUrl)
      .setAppName(appName)
      .set("spark.port.maxRetries", "100")
    val Spark = SparkSession.builder().config(sparkconf).getOrCreate()
    Spark
  }
def main(args: Array[String]): Unit = {
    val spark = getSparkSession()
    val sentenceDataFrame = spark.createDataFrame(Seq(
      (0, "Hi I heard about Spark"),
      (1, "I wish Java could use case classes"),
      (2, "Logistic regression models are neat")
    )).toDF("label", "sentence")
    sentenceDataFrame.show()
  }
```
假设要将 `sentence` 这一列拼接成一长串字符串，则：

```
sentenceDataFrame.createOrReplaceTempView("BIGDATA")
val sqlresult: DataFrame = spark.sql(s"SELECT sentence FROM BIGDATA")
val a: RDD[String] = sqlresult.rdd.map(_.getAs[String]("sentence"))
val b = a.reduce((x, y) => x + "," + y)
```

要是将 `sentence` 这一列拼接一个 `List`，则：

```
val c: RDD[List[String]] = sqlresult.rdd.map{ row=>List(row.getAs[String]("sentence"))}
val d: List[String] = c.reduce((x, y)=>x++y)
```