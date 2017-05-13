#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re
import requests

# 正则表达式
def reg(html):
    reg = r'("objURL":")(.+?)(",)'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist
# http://search.smzdm.com/?c=home&s=rimowa
# http://blog.csdn.net/eric_sunah/article/details/11099295

# 新建头部
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'),
					 ('Referer','http://search.smzdm.com/?c=home&s=rimowa'),
					 ('Host', 'search.smzdm.com')]

# 加载头部
urllib.request.install_opener(opener)

url = "http://search.smzdm.com/?c=home&s=rimowa"
# html_bytes = urllib.request.urlopen(url).read()
# html = html_bytes.decode("UTF-8")
# print(html)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    'Referer': 'http://search.smzdm.com/?c=home&s=rimowa',
    'Host': 'search.smzdm.com'}

html_bytes = requests.get(url=url, headers=header)
html = html_bytes.content.decode("UTF-8")
print(html)