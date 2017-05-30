#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# https://passport.baidu.com/v2/?login
url = "https://www.baidu.com/"

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get(url)

# 清空搜索框
browser.find_element_by_id("kw").clear()

# 通过id方式定位
browser.find_element_by_id("kw").send_keys("TTyb")

# 点击“百度一下”
browser.find_element_by_id("su").click()

while True:
    # 获得网页信息
    html = browser.page_source
    time.sleep(2)

    if "百哥么么哒|个人网站" in html:
        # 找到网页下所有的<a></a>
        lines = browser.find_elements_by_tag_name("a")
        for line in lines:
            # 获取<a></a>中的文本
            title = line.get_attribute("text")
            # 如果是正确的文本，那么提取其url
            if "百哥么么哒|个人网站" in title:
                ttyb_url = line.get_attribute("href")
                # 进入这个网页
                browser.get(ttyb_url)
        break
    else:
        # 点击下一页
        links = browser.find_elements_by_class_name("n")
        for link in links:
            text = link.get_attribute("text")
            if "下一页" in text:
                link.click()

browser.quit()
