---
layout: post
categories: [python]
title: python将字符串类型list转换成list
date: 2018-09-14
author: TTyb
desc: "python读取了一个list是字符串形式的[11.23,23.34]，想转换成list类型"
---

python读取了一个list是字符串形式的'[11.23,23.34]'，想转换成list类型：

# 方式一：

~~~ruby
import ast

str_list = "[11.23,23.34]"
list_list = ast.literal_eval(str_list)
print(type(list_list))
~~~


得到结果为：

~~~ruby
<class 'list'>
~~~

# 方式二：

~~~ruby
import json

str_list = "[11.23,23.34]"
list_list = json.loads(str_list)
print(type(list_list))
~~~


得到结果为：

~~~ruby
<class 'list'>
~~~