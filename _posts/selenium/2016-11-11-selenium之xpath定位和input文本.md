---
layout: post
categories: [selenium]
title: selenium之xpath定位和input文本
date: 2016-11-11
author: TTyb
desc: "selenium之xpath定位和input文本"
---

xpath简单定位：

> 1. 打开浏览器的F12

> 2. 在自己需要定位的元素的那里右键

> 3. 选择copy->xpath

<p style="text-align:center"><img src="/static/postimage/selenium/xpath/996148-20161111111028030-1563605392.png" class="img-responsive"/></p>

selenium获取input下的文本：

~~~ruby
driver.find_element_by_tag_name('input').get_attribute('value')
~~~