#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re

# 正则表达式
def reg(html):
    reg = r'({"img":")(.+?)(","title)'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist

url = "http://www.tybai.com/"
html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")
# print(html)

imgurls = reg(html)
# 图片名字
imgname = 1
for imgurl in imgurls:
    saveimg = open("E:/" + str(imgname) + ".jpg", 'wb')
    newimgurl = "http://www.tybai.com/" + imgurl[1].replace("\\", "")
    print(newimgurl)
    saveimg.write(urllib.request.urlopen(newimgurl).read())
    imgname += 1
    saveimg.close()