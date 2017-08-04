---
layout: post
categories: [scala]
title: spark No FileSystem for scheme file 解决方法
date: 2017-08-04
author: TTyb
desc: "在给代码带包成jar后，放到环境中运行出现No FileSystem for scheme file错误，找到解决办法"
---

在给代码带包成jar后，放到环境中运行出现如下错误：

```
Exception in thread "main" java.io.IOException: No FileSystem for scheme: file
	at org.apache.hadoop.fs.FileSystem.getFileSystemClass(FileSystem.java:2644)
	at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:2651)
	at org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:92)
	at org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:2687)
	at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:2669)
	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:371)
	at org.apache.hadoop.fs.Path.getFileSystem(Path.java:295)
	at org.apache.spark.sql.catalyst.catalog.SessionCatalog.makeQualifiedPath(SessionCatalog.scala:115)
	at org.apache.spark.sql.catalyst.catalog.SessionCatalog.createDatabase(SessionCatalog.scala:145)
	at org.apache.spark.sql.catalyst.catalog.SessionCatalog.<init>(SessionCatalog.scala:89)
	at org.apache.spark.sql.internal.SessionState.catalog$lzycompute(SessionState.scala:95)
	at org.apache.spark.sql.internal.SessionState.catalog(SessionState.scala:95)
	at org.apache.spark.sql.internal.SessionState$$anon$1.<init>(SessionState.scala:112)
	at org.apache.spark.sql.internal.SessionState.analyzer$lzycompute(SessionState.scala:112)
	at org.apache.spark.sql.internal.SessionState.analyzer(SessionState.scala:111)
	at org.apache.spark.sql.execution.QueryExecution.assertAnalyzed(QueryExecution.scala:49)
	at org.apache.spark.sql.Dataset$.ofRows(Dataset.scala:64)
	at org.apache.spark.sql.SparkSession.baseRelationToDataFrame(SparkSession.scala:382)
	at org.apache.spark.sql.DataFrameReader.load(DataFrameReader.scala:143)
	at org.apache.spark.sql.DataFrameReader.load(DataFrameReader.scala:122)
	at org.elasticsearch.spark.sql.EsSparkSQL$.esDF(EsSparkSQL.scala:52)
	at org.elasticsearch.spark.sql.EsSparkSQL$.esDF(EsSparkSQL.scala:66)
	at org.elasticsearch.spark.sql.package$SparkSessionFunctions.esDF(package.scala:58)
	at SQLAttack$.getDayDataByES(SQLAttack.scala:51)
	at SQLAttack$.main(SQLAttack.scala:25)
	at SQLAttack.main(SQLAttack.scala)
```

这是因为 `HDFS` 的配置文件没写好，更改方式如下：

找到自己项目保存库的位置，依次点击：

> File -> Settings -> Build,Execution,Deployment -> Build Tools -> Maven -> Local repository

这里的 `Local repository` 就是项目保存库的位置。在这里面依次打开文件位置：

> \repository\org\apache\hadoop\hadoop-common\2.7.2\

用 `rar` 打开 `hadoop-common-2.7.2.jar` ，把里面的 `core-default.xml` 下载到本地，打开添加更改，在 `<!--- global properties -->` 添加如下字段：

```
<!--- global properties -->
<property>
        <name>fs.hdfs.impl</name>
        <value>org.apache.hadoop.hdfs.DistributedFileSystem</value>
        <description>The FileSystem for hdfs: uris.</description>
</property>
<property>
        <name>fs.file.impl</name>
        <value>org.apache.hadoop.fs.LocalFileSystem</value>
        <description>The FileSystem for hdfs: uris.</description>
</property>
```

将更改后的 `core-default.xml` 重新放入 `hadoop-common-2.7.2.jar` 中，再次打包就可以运行了

