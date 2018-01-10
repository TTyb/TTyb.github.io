---
layout: post
categories: [scala]
title: dataframe的select传入不定参数
date: 2018-01-10
author: TTyb
desc: "在提取dataframe里面的列时，需要传入不定参数，即dataframe.select(args)"
---

在提取 `dataframe` 里面的列时，需要传入不定参数，即 `dataframe.select(args)` 。例如某个 `dataframe` 如下：

一般提取某列或者某几列的时候是这样子写的：

~~~ruby
dataframe.select("id", "col1", "col2")
~~~

但是有需求需要传入不定参数提取不定的列，则可以将需要提取的列放入到一个 `Array` 中，再如此调用：

~~~ruby
dataframe.select(Array.head, Array.tail: _*)
~~~

因为 `select` 官方定义的时候是支持传入不定参数的：

~~~ruby
def select(col: String, cols: String*): DataFrame = select((col +: cols).map(Column(_)) : _*)
~~~

唯一的要求是 `Array` 里面元素的类型是 `String` 类型。