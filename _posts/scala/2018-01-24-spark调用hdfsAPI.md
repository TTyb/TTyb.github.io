---
layout: post
categories: [scala]
title: spark调用hdfsAPI
date: 2018-01-24
author: TTyb
desc: "spark调用hdfsAPI查询文件名字、删除文件"
---

`spark` 调用 `hdfs` `API` 查询文件名字、删除文件：

### 获取HDFS上面某个路径下的所有文件的名字

~~~ruby
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.{FileUtil, Path}
val configuration = new Configuration()
val output = new Path(filePath)
val hdfs = output.getFileSystem(configuration)
val fs = hdfs.listStatus(output)
val fileName = FileUtil.stat2Paths(fs)
hdfs.close()
~~~

### 删除HDFS上面某个文件

~~~ruby
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.Path
val configuration = new Configuration()
val output = new Path(fileName)
val hdfs = output.getFileSystem(configuration)
hdfs.delete(output, true)
hdfs.close()
~~~