---
layout: post
categories: [python]
title: Windows7下安装pyspark
date: 2018-08-27
author: TTyb
desc: "在Windows7下需要安装pyspark，写下教程步骤"
---

安装需要如下东西：

##### java

[jdk-8u181-windows-x64.exe](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

##### spark

[spark-2.1.3-bin-hadoop2.7](http://spark.apache.org/downloads.html)

<p style="text-align:center"><img src="/static/postimage/python/pyspark/996148-20180827172721925-146345001.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

##### hadoop(版本要与spark的一致，这里都是hadoop2.7)

[hadoop-2.7.7](https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/ )

##### Anaconda(这个是为了预防python出现api-ms-win-crt-runtime-l1-1-0.dll错误，且安装了[vc_redist.2015.exe](https://www.microsoft.com/zh-CN/download/details.aspx?id=48145)还无法解决时需要安装)

[Anaconda3-2.4.1-Windows-x86_64.exe](https://www.anaconda.com/download/)

##### python

[python-3.5.4-amd64.exe](https://www.python.org/downloads/release/python-354/)

##### pycharm

[pycharm-community-2016.1.4.exe]()

# 安装JDK

** 千万不要用默认路径Program Files，这个有空格后面会很坑！新建路径在C:\Java，Java安装在这里！**

>1. 新建环境变量名：JAVA_HOME，变量值：C:\Java\jdk1.8.0_11
>2. 打开PATH，添加变量值：%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin
>3. 新建环境变量名：CLASSPATH，变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar

在 `cmd` 中输入 `java` 出现如下信息就算安装成功了

<p style="text-align:center"><img src="/static/postimage/python/pyspark/996148-20180827174102585-1120519592.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

# 安装spark

在C盘新建`Spark`目录，将其解压到这个路径下

<p style="text-align:center"><img src="/static/postimage/python/pyspark/996148-20180827174335102-1580663783.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

>1. 新建环境变量名：SPARK_HOME，变量值：C:\Spark
>2. 打开PATH，添加变量值：%SPARK_HOME%\bin

# 安装hadoop

在C盘新建`Hadoop`目录，将其解压到这个路径下

>1. 新建环境变量名：HADOOP_HOME，变量值：C:\Hadoop
>2. 打开PATH，添加变量值：%HADOOP_HOME%\bin

去网站下载Hadoop在Windows下的支持winutils

[https://github.com/steveloughran/winutils](https://github.com/steveloughran/winutils)

根据版本来选择，这里用的是 `hadoop2.7`，所以选择`2.7`的`bin`下载下来，将其覆盖到 `C:\Hadoop\bin`

修改C:\Hadoop\etc\hadoop下的hadoop-env.cmd为set JAVA_HOME=C:\Java\jdk1.8.0_11

在 `cmd` 中输入 `hadoop` 出现如下信息就算安装成功了

<p style="text-align:center"><img src="/static/postimage/python/pyspark/996148-20180827175324797-2114740128.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

# 安装python

安装路径为 `C:\Python35`

在C盘或者代码盘新建\tmp\hive路径，输入命令

```
winutils.exe chmod -R 777 C:\tmp\hive
```

# 验证pyspark

cmd输入pyspark得到如下画面

<p style="text-align:center"><img src="/static/postimage/python/pyspark/996148-20180828094521822-1954353945.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

# 配置pycharm

在如下路径添加环境变量

>1. JAVA_HOME
>2. SPARK_HOME
>3. HADOOP_HOME

```
Run->Edit Configurations->Environment variables
```

<p style="text-align:center"><img src="/static/postimage/python/pyspark/996148-20180828094945469-1030294840.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>