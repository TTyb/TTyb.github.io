---
layout: post
categories: [scala]
title: spark DenseVector to SparseVector
date: 2019-07-05
author: TTyb
desc: "在使用 `import org.apache.spark.ml.feature.VectorAssembler` 转换特征后，想要放入 `import org.apache.spark.mllib.classification.SVMWithSGD` 去训练的时候出现错误"
---

在使用 `import org.apache.spark.ml.feature.VectorAssembler` 转换特征后，想要放入 `import org.apache.spark.mllib.classification.SVMWithSGD` 去训练的时候出现错误：

~~~ruby
Caused by: java.lang.ClassCastException: org.apache.spark.ml.linalg.DenseVector cannot be cast to org.apache.spark.ml.linalg.SparseVector
~~~

修改如下：

~~~ruby
val trainDataFrame = dataframe.rdd.map(r => LabeledPoint(
  r.getAs[Double]("label"),
org.apache.spark.mllib.linalg.Vectors.fromML(r.getAs[org.apache.spark.ml.linalg.SparseVector]("features").toDense)

))
~~~