#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re
from lxml import etree


# 正则表达式
def reg(html):
    reg = r"(<marquee)(.+?)(>)(.+?)(</marquee>)"
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist[0][3]


url = "http://www.tybai.com"

html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")
print(html)
# print(reg(html))

# 初始化网页
soup = BeautifulSoup(html, "html.parser")
# info = soup.find("marquee").get_text()
# infos = soup.find_all("span", attrs={"class": "label"})
# for info in infos:
#     print(info.get_text())

# 初始化网页
page = etree.HTML(html.lower())
# text = page.xpath('//marquee/text()')
text = page.xpath('//*[@id="footer"]/ul/li[1]/a/span/text()')
print(text)