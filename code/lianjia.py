#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
           'Referer': 'm.lianjia.com',
           'Host': 'm.lianjia.com',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
           'Connection': 'keep-alive'
           }

session = requests.session()
print("第一次访问：获取set-cookie")
session.get("https://m.lianjia.com/", headers=headers)
html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)


def getHtml(url, _cookie=None):
    # 解析网页
    html_bytes = session.get(url, headers=headers, cookies=_cookie)
    html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    return html_set_cookie, html_bytes.content.decode("utf-8", "ignore")


# 获取城市对应的缩写
def getCity(html):
    cityDict = {}
    soup = BeautifulSoup(html, "html.parser")
    citys = soup.find_all("div", attrs={"class": "city_block"})
    for city in citys:
        list_tmp = city.find_all('a')
        for a in list_tmp:
            cityHref = a.get('href')
            cityName = a.get_text()
            cityDict[cityName] = cityHref

    return cityDict


# 获取引导频道二手房、新房、查成交、找小区
def getChannel(html):
    channelDict = {}
    soup = BeautifulSoup(html, "html.parser")
    channels = soup.find_all("a", attrs={"class": "inner post_ulog"})
    for channel in channels:
        list_tmp = channel.find_all("div", attrs={"class": "name"})
        channelName = list_tmp[0].get_text()
        channelHref = channel.get('href')
        channelDict[channelName] = channelHref
    return channelDict

if __name__ == "__main__":
    url_ori = "https://m.lianjia.com/"

    city = "广州"
    url_get_city = url_ori + "/city/"
    print("第二次访问：获取城市编码")
    html_set_cookie, html_city = getHtml(url_get_city)
    # print(html_city)
    cityDict = getCity(html_city)
    # https://m.lianjia.com/gz/
    url_city = url_ori + cityDict[city]
    print("第三次：访问获取导航")
    html_set_cookie, html_city_content = getHtml(url_city, _cookie=html_set_cookie)
    channelDict = getChannel(html_city_content)
    channel = "二手房"
    url_channel = url_ori + channelDict[channel]

    print("第四次访问：获取房子信息")
    html_set_cookie,html_houses_content = getHtml(url_channel,_cookie=html_set_cookie)
    print(html_houses_content)
    print(html_set_cookie)


