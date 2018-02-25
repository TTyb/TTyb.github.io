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

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401170306727-2055561671.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

名字随便命名，到后面可以改的：

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401170825774-1018982829.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

存放代码项目的位置，名字还是随便命名，可以改的，但是路径要自定义好：

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401170845133-118406518.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

设置库包的存放位置，路径自行更改：

> file->setting->Build,Execution,Deployment->Build Tools->Maven

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401171244242-1208637823.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

> file->Project Structure

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401171550399-1063989275.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401171657977-158744880.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

加载 `scala` ，如果 `scala` 还没安装的话请看 [scala安装教程](http://www.tybai.com/scala/Scala%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B.html) :

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/TIM20170927104721.jpg" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/TIM20170927104730.jpg" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

加载新的库包：

在网站 `http://mvnrepository.com/` 里面可以找到

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401171739914-28231936.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

复制类似于 `XML` 的东西到 `pom.xml` 里面就好

<p style="text-align:center"><img src="/static/postimage/IDE/intellij/996148-20170401171719711-792682866.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>