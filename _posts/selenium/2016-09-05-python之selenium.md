---
layout: post
categories: [selenium]
title: python之selenium
date: 2016-09-05
author: TTyb
desc: "selenium是处理异步加载的一种方法"
---

selenium是处理异步加载的一种方法

总的来说是操作浏览器访问来获取自己想要的资料

优点是浏览器能看到的都能爬下来，简单有效，不需要深入破解网页加载形式 

缺点是加载的东西太多，导致爬取速度变慢

~~~ruby
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# http://www.cnblogs.com/fnng/p/3238685.html
# 打开火狐浏览器
browser = webdriver.Firefox()

# 输入网址
browser.get("http://www.baidu.com")
# 根据各自网速来判断网址加载时间
time.sleep(1)

# 输入框
# <input id="kw" class="s_ipt" type="text" maxlength="100" name="wd" autocomplete="off">

# 清空输入框
browser.find_element_by_id("kw").clear()

# 通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
# 通过name方式定位
# browser.find_element_by_name("wd").send_keys("selenium")
# 通过tag name方式定位
# browser.find_element_by_tag_name("input").send_keys("selenium")
# 通过class name 方式定位
# browser.find_element_by_class_name("s_ipt").send_keys("selenium")
# 通过CSS方式定位
# browser.find_element_by_css_selector("#kw").send_keys("selenium")
# 通过xphan方式定位
# browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

# 点击“百度一下”
browser.find_element_by_id("su").click()

# 下面就是xpath的知识了
# 想找那个网页的什么东西自己写xpath
# 可以参考前面的博客：http://www.cnblogs.com/TTyb/p/5832790.html
print(browser.find_element_by_xpath("//a"))
# 获得当前html
html = browser.page_source
time.sleep(5)
browser.quit()
~~~

