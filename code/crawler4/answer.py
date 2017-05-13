#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = "http://blog.csdn.net/eric_sunah/article/details/11099295"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    'Referer': 'http://blog.csdn.net/eric_sunah/article/details/11099295',
    'Host': 'blog.csdn.net'}

html_bytes = requests.get(url=url, headers=header)
html = html_bytes.content.decode("UTF-8")
print(html)

page = etree.HTML(html.lower())
img_src = page.xpath('//div[@id="blog_userface"]/a/img/@src')
print(img_src)

saveimg = open("E:/head.jpg", 'wb')
saveimg.write(requests.get(url=img_src[0]).content)
saveimg.close()