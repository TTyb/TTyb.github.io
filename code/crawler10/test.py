#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import requests
import time
import random
import json
import re
import threading

session = requests.session()

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
           'Referer':
               'http://image.baidu.com',
           'Host': 'image.baidu.com',
           'Accept': 'text/plain, */*; q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Connection': 'keep-alive'}


def get_tt():
    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    tt = str(nowtime) + str(timerandom)
    return tt


def getdata(nowtime, keyword, pn):
    postdata = {
        nowtime: "",
        "adpicid": "",
        "cl": "2",
        "ct": "201326592",
        "face": "0",
        "fp": "result",
        "fr": "",
        "gsm": "5a",
        "height": "",
        "ic": "0",
        "ie": "utf-8",
        "ipn": "rj",
        "is": "",
        "istype": "2",
        "lm": "-1",
        "nc": "1",
        "oe": "utf-8",
        "pn": pn,
        "qc": "",
        "queryWord": keyword,
        "rn": "30",
        "s": "",
        "se": "",
        "st": "-1",
        "tab": "",
        "tn": "resultjson_com",
        "width": "",
        "word": keyword,
        "z": ""
    }

    html_bytes = session.get(url="http://image.baidu.com/search/acjson?", params=postdata, headers=headers)

    jsondata = html_bytes.content.decode('utf-8', 'ignore')
    jsoninfo = json.loads(jsondata)

    return jsoninfo


def makeurl(thumbURL):
    urlhead = "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy"

    reg = r'(.com)(.+)'
    all = re.compile(reg)
    alllist = re.findall(all, thumbURL)
    newurl = urlhead + alllist[0][1]
    return newurl


def geturl(nowtime, keyword, pn):
    jsoninfo = getdata(nowtime, keyword, pn)

    urlarr = []
    for item in jsoninfo["data"]:
        try:
            thumbURL = item["thumbURL"]
            imgurl = makeurl(thumbURL)
            urlarr.append(imgurl)
            print(imgurl)
        except Exception as error:
            print(error)

    threadingrun(urlarr)


def downloadimg(imgurl, imgname):
    saveimg = open("E:/" + str(imgname) + ".jpg", 'wb')
    saveimg.write(session.get(url=imgurl, headers=headers).content)
    saveimg.close()


def threadingrun(array):
    imgname = 1
    # 创建线程池
    threadpool = []
    # 定义线程
    for imgurl in array:
        imgname += 1 + int(time.time())
        th = threading.Thread(target=downloadimg, args=(imgurl, imgname))
        threadpool.append(th)

        print(imgname)
    # 开始线程
    for th in threadpool:
        th.start()
    # 等待所有线程运行完毕
    for th in threadpool:
        th.join()


if __name__ == '__main__':
    nowtime = get_tt()
    keyword = "图片"
    pn = 30

    while True:
        geturl(nowtime, keyword, pn)
        pn += 60
        input("暂停")