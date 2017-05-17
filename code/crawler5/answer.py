#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import threading
import re
from concurrent.futures import ThreadPoolExecutor


# 正则表达式
def reg(html):
    reg = r'(<h3><a href=")(.+?)(">)'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist


def downloadhtml(htmlurl,htmlname):
    savehtml = open("E:/" + str(htmlname) + ".html", 'wb')
    html = urllib.request.urlopen(htmlurl).read()
    savehtml.write(html)
    savehtml.close()


if __name__ == '__main__':

    url = "http://www.tybai.com/topic"
    html_bytes = urllib.request.urlopen(url).read()
    html = html_bytes.decode("UTF-8")
    print(html)

    htmlurls = reg(html)
    htmlname = 0

    # threadpool = []
    # # 将任务加入线程
    # for htmlurl in htmlurls:
    #     newhtmlurl = "http://www.tybai.com/" + htmlurl[1].replace("\\", "")
    #     th = threading.Thread(target=downloadhtml, args=(newhtmlurl,htmlname))
    #     print(newhtmlurl)
    #     threadpool.append(th)
    #     htmlname += 1
    # # 开始线程
    # for th in threadpool:
    #     th.start()
    # # 等待所有线程运行完毕
    # for th in threadpool:
    #     th.join()

    # concurrent.futures
    pool = ThreadPoolExecutor(max_workers=100)
    # 将下载图片的任务加入线程
    for htmlurl in htmlurls:
        newhtmlurl = "http://www.tybai.com/" + htmlurl[1].replace("\\", "")
        pool.submit(downloadhtml, newhtmlurl, htmlname)
        htmlname += 1


