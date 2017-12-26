---
layout: post
categories: [scala]
title: spark System memory must be at least
date: 2017-12-26
author: TTyb
desc: "System memory * must be at least *.Please increase heap size using the --driver--memory option or spark.driver.memory"
---

运行 `ScalaSpark` 程序的时候出现错误：

```
System memory * must be at least *.Please increase heap size using the --driver--memory option or spark.driver.memory
```

<p style="text-align:center"><img src="/static/postimage/scala/systemmemory/20171226094546.png"/></p>

在 `Intellij IDEA` 里面找到：

```
Run -> Edit Configurations -> Application -> Configurations 
```

<p style="text-align:center"><img src="/static/postimage/scala/systemmemory/20171226095003.png"/></p>

设置大小：

```
-Xms256m -Xmx1024m
```

<p style="text-align:center"><img src="/static/postimage/scala/systemmemory/20171226095209.jpg"/></p>