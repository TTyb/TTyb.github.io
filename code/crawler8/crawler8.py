#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from selenium import webdriver

# https://passport.baidu.com/v2/?login
url = "https://passport.baidu.com/v2/?login"

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get(url)

# 清空账号输入框
browser.find_element_by_id("TANGRAM__PSP_3__userName").clear()
# 通过id方式定位账号
browser.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("username")

# 清空密码输入框
browser.find_element_by_id("TANGRAM__PSP_3__password").clear()
# 通过id方式定位密码
browser.find_element_by_id("TANGRAM__PSP_3__password").send_keys("password")

# 点击“登陆”
browser.find_element_by_id("TANGRAM__PSP_3__submit").click()

cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]

dict = {}
for item in cookie:
    itm = item.split("=")
    dict[itm[0]] = itm[1]

import json
file = open("cookie.json","w")
file.write(json.dumps(dict))
file.close()

browser.quit()
