---
layout: post
categories: [python]
title: python编译、运行、反编译pyc文件
date: 2017-04-21
author: TTyb
desc: "为了加密 `.py` 文件，以前一般使用打包成exe ，但是最近发现可以将其编译成二进制文件pyc，虽然反编译难度不大，但是也需要一些水平"
---

为了加密 `.py` 文件，以前一般使用打包成 `exe` ，但是最近发现可以将其编译成二进制文件 `pyc` ，虽然反编译难度不大，但是也需要一些水平

### 编译生成 `pyc`：

> 单个文件

代码：

~~~ruby
import py_compile
py_compile.compile("test.py")
~~~
命令行下：

~~~ruby
python -m py_compile test.py
~~~

> 多个文件

~~~ruby
import compileall
compileall.compile_dir("存放海量py的目录")
~~~

命令行下：

~~~ruby
python -m compileall 存放海量py的目录
~~~

### 运行 `pyc` 文件

命令行下：

~~~ruby
python test.pyc
~~~

<p style="text-align:center"><img src="/static/postimage/python/pyc/996148-20170421090418149-1426718335.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

### 反编译 `pyc`

首先安装库 `uncompyle`

`pip install uncompyle`

<p style="text-align:center"><img src="/static/postimage/python/pyc/996148-20170421090457681-111691906.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

查看 `uncompyle` 函数属性：

<p style="text-align:center"><img src="/static/postimage/python/pyc/996148-20170421090619806-263727698.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

命令行下：

~~~ruby
uncompyle6 test.pyc > test1.py
~~~

和源文件对比：

<p style="text-align:center"><img src="/static/postimage/python/pyc/996148-20170421091133056-1264995189.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>
