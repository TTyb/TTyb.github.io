#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
}

session = requests.session()
session.get("https://s.m.taobao.com/", headers=headers)


def getJson():
    getData = {
        "event_submit_do_new_search_auction": "1",
        "search": "提交",
        "tab": "all",
        "_input_charset": "utf-8",
        "topSearch": "1",
        "atype": "b",
        "searchfrom": "1",
        "action": "home:redirect_app_action",
        "from": "1",
        "q": "iphonex",
        "sst": "1",
        "n": "20",
        "buying": "buyitnow",
        "m": "api4h5",
        "abtest": "30",
        "wlsort": "30",
        "style": "list",
        "closeModues": "nav,selecthot,onesearch",
        "page": "2"
    }

    preUrl = "http://s.m.taobao.com/search?"
    # 升级头部
    headers.update(
        dict(Referer="http://s.m.taobao.com", Host="s.m.taobao.com"))
    # 抓取网页
    aliUrl = session.get(url=preUrl, params=getData, headers=headers)

    return aliUrl.content


def main():
    jsonInfo = getJson()
    file = open("html.json", 'wb')
    file.write(jsonInfo)
    file.close()
    print(jsonInfo)


if __name__ == "__main__":
    main()
