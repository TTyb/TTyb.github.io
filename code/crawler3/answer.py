#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
from lxml import etree


url = "http://www.tybai.com"

html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")
print(html)

# 初始化网页
soup = BeautifulSoup(html, "html.parser")
# for myimg in soup.find_all('section', id='intro'):
#     img_src = myimg.find('img').get('src')
#     saveimg = open("E:/head.jpg", 'wb')
#     imgurl = "http://www.tybai.com/" + img_src
#     saveimg.write(urllib.request.urlopen(imgurl).read())
#     saveimg.close()

# 初始化网页
page = etree.HTML(html.lower())
img_src = page.xpath('//section[@id="intro"]/img/@src')

saveimg = open("E:/head.jpg", 'wb')
imgurl = "http://www.tybai.com/" + img_src[0]
saveimg.write(urllib.request.urlopen(imgurl).read())
saveimg.close()