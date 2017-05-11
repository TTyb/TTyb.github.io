#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re
from lxml import etree


# 正则表达式
def reg(html):
    reg = r'(<th><span class="topicc">)(.+?)(.html">)(.+?)(</a></span></th>)'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist


url = "http://www.tybai.com/category"
html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")
print(html)

# 正则表达式获得标题
# alllist = reg(html)
# for item in alllist:
#     print(item[3])

# BeautifulSoup获得标题
# soup = BeautifulSoup(html, "html.parser")
# infos = soup.find_all("span", attrs={"class": "topicc"})
# for info in infos:
#     print(info.get_text())

# lxml获得标题
page = etree.HTML(html.lower())
text = page.xpath('//span[@class="topicc"]/a/text()')
print(text)