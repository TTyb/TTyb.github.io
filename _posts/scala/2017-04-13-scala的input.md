---
layout: post
categories: [scala]
title: scala的input
date: 2017-04-13
author: TTyb
desc: "scala的input"
---

获取用户输入的信息，一般使用 `input` 函数，但是 `scala` 里面是没有 `input` 这个方法的，为了获取控制台的输入操作， `scala` 定义的方法为：

~~~ruby
val Inputcontent = Console.readLine()
~~~