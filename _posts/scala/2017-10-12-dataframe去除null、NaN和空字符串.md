---
layout: post
categories: [scala]
title: dataframe去除null、NaN和空字符串
date: 2017-10-12
author: TTyb
desc: "一种去除dataframe中null、NaN和空字符串的方法，基于scala下"
---

### 去除null、NaN

去除 `dataframe` 中的 `null` 、 `NaN` 有方法 `drop` ，用 `dataframe.na` 找出带有 `null`、 `NaN` 的行，用 `drop` 删除行：

~~~ruby
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{DataFrame, SQLContext, SparkSession}
/**
  * Created by TTyb on 2017/10/12.
  */
object test3 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("TTyb").setMaster("local")
    val sc = new SparkContext(conf)
    val spark=new SQLContext(sc)
    val sentenceDataFrame = spark.createDataFrame(Seq(
      (1, "asf"),
      (2, "2143"),
      (3, "rfds"),
      (4, null),
      (5, "")
    )).toDF("label", "sentence")
    sentenceDataFrame.show()
    sentenceDataFrame.na.drop().show()
  }
}
~~~

### 去除空字符串

去除空字符串用 `dataframe.where` ：

~~~ruby
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{DataFrame, SQLContext, SparkSession}
/**
  * Created by TTyb on 2017/10/12.
  */
object test3 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("TTyb").setMaster("local")
    val sc = new SparkContext(conf)
    val spark=new SQLContext(sc)
    val sentenceDataFrame = spark.createDataFrame(Seq(
      (1, "asf"),
      (2, "2143"),
      (3, "rfds"),
      (4, null),
      (5, "")
    )).toDF("label", "sentence")
    sentenceDataFrame.show()
    // sentenceDataFrame.na.drop().show()
    sentenceDataFrame.where("sentence <> ''").show()
  }
}
~~~
