---
layout: post
categories: [python]
title: python之chardet库识别编码
date: 2017-08-24
author: TTyb
desc: "chardet库是python的字符编码检测器，能够检测出各种编码的类型"
---

chardet库是python的字符编码检测器，能够检测出各种编码的类型，例如：

```
import chardet
import urllib.request
 
testdata = urllib.request.urlopen('http://m2.cn.bing.com/').read()
print(chardet.detect(testdata))
```

运行结果：

```
{'confidence': 0.99, 'encoding': 'utf-8'}
```

翻译一下就是：

```
{'精准度': 99%, 'encoding(编码形式)': 'utf-8'}
```

没见识到这个库之前所有编码纯属自己的记忆：

```
# unicode_escape
\u4e2d\u56fd
# gbk或者utf-8
\xd6\xd0\xb9\xfa
中国
# urlencode
%e4%b8%ad%e5%9b%bd
# Gb2312
%d6%d0%b9%fa
```

这些编码纯属需要眼睛辨认再去网上查找编码，现在发现了chardet这个库后方便了很多　　