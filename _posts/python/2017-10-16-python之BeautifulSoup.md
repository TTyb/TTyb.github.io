---
layout: post
categories: [python]
title: python之BeautifulSoup
date: 2017-10-16
author: TTyb
desc: "python之BeautifulSoup使用"
---

爬虫有时候写正则表达式会有假死现象

就是正则表达式一直在进行死循环查找

例如：https://social.msdn.microsoft.com/forums/azure/en-us/3f4390ac-11eb-4d67-b946-a73ffb51e4f3/netcpu100

所以一般在解析网页的时候可以用BeautifulSoup库来解决网页的正则表达式

网上对于BeautifulSoup的解释太复杂了

我就只是选取了我爬虫需要的部分来学习，其他的有需要再去学习，没需要就不浪费时间

最起码省心了很多

解释在注释里面都有了

一句一句的打印出来看就会明白的

~~~ruby
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "http://www.lenggirl.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Referer': None
    }
    data = urllib.request.urlopen(url).read()
    # ('UTF-8')('unicode_escape')('gbk','ignore')
    data = data.decode('UTF-8', 'ignore')
    # 初始化网页
    soup = BeautifulSoup(data, "html.parser")
    # 打印整个网页
    html = soup.prettify()
    # 打印<head>...</head>
    head = soup.head
    # 打印<body>...</body>
    body = soup.body
    # 打印第一个<p>...</p>
    p = soup.p
    # 打印p的内容
    p_string = soup.p.string
    # soup.p.contents[0]为Aug 22, 2016
    # soup.p.contents为[' Aug 22, 2016\n                        ']
    p_string = soup.p.contents[0]
    # 将body里面的所有头打印出来
    for child in soup.body.children:
        #print(child)
        pass
    # 将所有的<a>...</a>和<p>...</p>打印出来
    a_and_p = soup.find_all(["a","p"])
    # 找到<a>...</a>下所有的网址
    for myimg in soup.find_all('a'):
        img_src = myimg.get('href')
        #print(img_src)
    # 找到<a>...</a>下类为class_='a'下面的<img>...</img>里面的src
    for myimg in soup.find_all('a', attrs={'class':'a'}):
        img_src = myimg.find('img').get('src')
    # 网页所有信息
    #print(html)
~~~
