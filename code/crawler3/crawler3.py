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
	
# 使用urlretrieve下载图片
def cbk(a, b, c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)
	
for imgurl in imgurls:
    work_path = "E:/" + str(imgname) + ".jpg"
    saveimg = open("E:/" + str(imgname) + ".jpg", 'wb')
    newimgurl = "http://www.tybai.com/" + imgurl[1].replace("\\", "")
    urllib.request.urlretrieve(newimgurl, work_path, cbk)
    imgname += 1