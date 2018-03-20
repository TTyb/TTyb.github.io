#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import threading
import re
from concurrent.futures import ThreadPoolExecutor


# 正则表达式
def reg(html):
    reg = r'(<img src=")(.+?)(" alt="")'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist


def downloadimg(imgurl,imgname):
    saveimg = open("E:/" + str(imgname) + ".jpg", 'wb')
    saveimg.write(urllib.request.urlopen(imgurl).read())
    saveimg.close()


if __name__ == '__main__':

    url = "http://www.tybai.com/"
    html_bytes = urllib.request.urlopen(url).read()
    html = html_bytes.decode("UTF-8")
    print(html)

    imgurls = reg(html)
    imgname = 0

    # threadpool = []
    # # 将任务加入线程
    # for imgurl in imgurls:
    #     newimgurl = "http://www.tybai.com" + imgurl[1]
    #     th = threading.Thread(target=downloadimg, args=(newimgurl,imgname))
    #     threadpool.append(th)
    #     imgname += 1
    # # 开始线程
    # for th in threadpool:
    #     th.start()
    # # 等待所有线程运行完毕
    # for th in threadpool:
    #     th.join()

    #
    pool = ThreadPoolExecutor(max_workers=11)
    # 将下载图片的任务加入线程
    for imgurl in imgurls:
        newimgurl = "http://www.tybai.com" + imgurl[1]
        pool.submit(downloadimg, newimgurl, imgname)
        imgname += 1


