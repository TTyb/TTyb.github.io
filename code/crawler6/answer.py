#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import random


def gethtml(url, postdata):
    header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
              'Referer': 'https://www.baidu.com/',
              'Host': 'sp0.baidu.com',
              'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
              'Connection': 'keep-alive'
              }

    # 解析网页
    html_bytes = requests.get(url, headers=header, params=postdata)

    return html_bytes.content


def getnowtime():
    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    return str(nowtime) + str(timerandom)


if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    # keyword = "TTyb|个人网站"

    keyword = input("请输入你要搜索的关键词：")

    # 抓取页数需要增加 pn
    # pn = 0 第一页
    # pn = 10 第二页
    # 确定方式以百度的logo位置 <i class="c-icon c-icon-bear-p">
    # 如果logo的代码包裹的是1：<strong><span class="fk fk_cur"><i class="c-icon c-icon-bear-p"></i></span><span class="pc">1</span></strong>
    # 如果logo的代码包裹的是2：<strong><span class="fk fk_cur"><i class="c-icon c-icon-bear-p"></i></span><span class="pc">2</span></strong>

    # 构造postdata
    postdata = {
        '_': getnowtime(),
        'bs': keyword,
        'cb': "jQuery110207635110323506591_1495027071143",
        'csor': 18,
        'json': 1,
        'p': 3,
        'pbs': keyword,
        'pwd': keyword,
        'req': 2,
        'sid': "1432_21085_17001_20927",
        'sugmode': 2,
        'wd': keyword,
        'pn':10
    }

    html_bytes = gethtml(url, postdata)
    html = html_bytes.decode("utf-8", "ignore")
    print(html)
