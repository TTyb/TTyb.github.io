---
layout: post
categories: [IDE]
title: IntelliJ的Scala配置
date: 2017-04-01
author: TTyb
desc: "IntelliJ的Scala配置"
---

打开IDE：

> file->New->Project->Maven->Next

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401170306727-2055561671.png)

名字随便命名，到后面可以改的：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401170825774-1018982829.png)

存放代码项目的位置，名字还是随便命名，可以改的，但是路径要自定义好：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401170845133-118406518.png)

设置库包的存放位置，路径自行更改：

> file->setting->Build,Execution,Deployment->Build Tools->Maven

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401171244242-1208637823.png)

> file->Project Structure

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401171550399-1063989275.png)

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401171657977-158744880.png)

加载新的库包：

在网站 `http://mvnrepository.com/` 里面可以找到

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401171739914-28231936.png)

复制类似于 `XML` 的东西到 `pom.xml` 里面就好

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170401171719711-792682866.png)