#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

url = "https://www.baidu.com/"

browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

# 填写TTyb
browser.find_element_by_id("index-kw").send_keys("TTyb")
# 填写完后按回车键
browser.find_element_by_id("index-kw").send_keys(Keys.ENTER)

while True:
    print(1)
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
        break
    else:
        try:
            # 点击下一页
            link_first = browser.find_elements_by_class_name("new-nextpage-only")
            browser.get(link_first[0].get_attribute("href"))
        except:
            link_after = browser.find_elements_by_class_name("new-nextpage")
            browser.get(link_after[0].get_attribute("href"))


# 捕获所有的句柄
handles = browser.window_handles
# 窗口切换，切换为新打开的窗口
browser.switch_to_window(handles[-1])

html = browser.page_source
if "百哥么么哒" in html:
    print("成功")