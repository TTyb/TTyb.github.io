---
layout: post
categories: [selenium]
title: selenium设置Chrome
date: 2016-12-03
author: TTyb
desc: "selenium设置浏览器属性"
---

### 关闭图片

```
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options)

# browser = webdriver.Chrome()
url = "http://image.baidu.com/"
browser.get(url)
input("是否有图")
browser.quit()

```

![](http://images2015.cnblogs.com/blog/996148/201612/996148-20161203114330787-1216998587.png)

### 更改UA和语言

```
# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

from selenium import webdriver
# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
browser = webdriver.Chrome(chrome_options=options)
url = "http://image.baidu.com/"
browser.get(url)
browser.quit()
```

![](http://images2015.cnblogs.com/blog/996148/201612/996148-20161203115018521-1738483123.png)

### 携带cookie

```
# !/usr/bin/python3.4
# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()

url = "https://www.baidu.com/"
browser.get(url)
# 通过js新打开一个窗口
newwindow='window.open("https://www.baidu.com");'
# 删除原来的cookie
browser.delete_all_cookies()
# 携带cookie打开
browser.add_cookie({'name':'ABC','value':'DEF'})
# 通过js新打开一个窗口
browser.execute_script(newwindow)
input("查看效果")
browser.quit()
```

![](http://images2015.cnblogs.com/blog/996148/201612/996148-20161205140547554-2049984391.png)