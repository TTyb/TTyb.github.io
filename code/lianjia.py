#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
           'Referer': 'm.lianjia.com',
           'Host': 'm.lianjia.com',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
           'Connection': 'keep-alive'
           }

session = requests.session()
url_ori = "https://m.lianjia.com/"
print("第一次访问：获取set-cookie", "：", url_ori)
session.get(url_ori, headers=headers)
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


# 获取真正房子的详细信息
def getDetail(html):
    detailArr = []

    soup = BeautifulSoup(html, "html.parser")
    detailInfo = soup.find_all("div", attrs={"class": "item_list"})
    detailUrl = soup.find_all("a", attrs={"class": "a_mask"})
    details = zip(detailInfo,detailUrl)
    for info_url in details:
        info = info_url[0]
        detailDict = {}
        # 获取标题
        title_tmp = info.find_all("div", attrs={"class": "item_main"})
        detail_title = title_tmp[0].get_text()
        # 获取房屋大小
        size_tmp = info.find_all("div", attrs={"class": "item_other"})
        detail_size = size_tmp[0].get_text()
        # 获取价格单价
        price_total_tmp = info.find_all("span", attrs={"class": "price_total"})
        detail_price_total = price_total_tmp[0].get_text()
        unit_price_tmp = info.find_all("span", attrs={"class": "unit_price"})
        detail_unit_price = unit_price_tmp[0].get_text()
        # 获取标签
        tag_tmp = info.find_all("div", attrs={"class": "tag_box"})
        detail_tag = tag_tmp[0].get_text()
        # 获取详情页
        url_a = info_url[1]

        detailDict["title"] = detail_title
        detailDict["size"] = detail_size
        detailDict["room"] = detail_size.split("/")[0]
        detailDict["room_size"] = detail_size.split("/")[1]
        detailDict["room_toward"] = detail_size.split("/")[2]
        detailDict["room_name"] = detail_size.split("/")[3]
        detailDict["price_total"] = detail_price_total
        detailDict["price_t"] = int(detail_price_total.replace("万",""))
        detailDict["price_f"] = int(detail_price_total.replace("万",""))*0.3
        detailDict["unit_price"] = detail_unit_price
        detailDict["u_price"] = int(detail_unit_price.replace("元/平",""))
        detailDict["tag"] = detail_tag
        detailDict["url"] = url_ori + url_a.get("href")
        detailArr.append(detailDict)
    return detailArr


# 获取json
def getDetailJson(html_set_cookie, pages):
    allList = []
    for i in range(pages):
        page = i + 1
        headerJson = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
                      'Referer': 'https://m.lianjia.com/gz/ershoufang/pg' + str(page) + '/',
                      'Host': 'm.lianjia.com',
                      'Accept': 'application/json',
                      'Accept-Encoding': 'gzip, deflate',
                      'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                      'X-Requested-With': 'XMLHttpRequest',
                      'Connection': 'keep-alive'
                      }
        url_detail = "https://m.lianjia.com/gz/ershoufang/pg" + str(page) + "/?_t=1"
        print("模拟请求：获取房子详情", "：", url_detail)
        html_bytes = session.get(url_detail, headers=headerJson, cookies=html_set_cookie)
        html_detail = html_bytes.content.decode("utf-8", "ignore")
        detailJson = json.loads(html_detail)
        detailArr = getDetail(detailJson["body"])
        allList = allList + detailArr
        time.sleep(2)

    return allList

# 获取便宜的房子
def getHotHouse(allList,room):
    df = pd.DataFrame(allList)
    # 根据首付降序排列
    df["rank"] = df['price_f'].rank(ascending=1, method='dense')
    # 选出首付最低的10个且三房的
    df_rank = df[df["rank"] <= 10]
    df_room = df_rank[df_rank["room"].str.contains(room)]

    return df_room

# main函数
def getHtmlMain(city, channel, pages, room):
    url_get_city = url_ori + "/city/"
    print("第二次访问：获取城市编码", "：", url_get_city)
    html_set_cookie, html_city = getHtml(url_get_city)
    cityDict = getCity(html_city)
    url_city = url_ori + cityDict[city]
    print("第三次访问：访问获取导航", "：", url_city)
    html_set_cookie, html_city_content = getHtml(url_city, _cookie=html_set_cookie)
    channelDict = getChannel(html_city_content)
    url_channel = url_ori + channelDict[channel]
    print("第四次访问：获取房子信息", "：", url_channel)
    html_set_cookie, html_houses_content = getHtml(url_channel, _cookie=html_set_cookie)
    allList = getDetailJson(html_set_cookie, pages)
    print("获取优质房子")
    resultHouse = getHotHouse(allList,room)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 1000)
    print(resultHouse)

if __name__ == "__main__":
    city = "广州"
    channel = "二手房"
    pages = 2
    room = "3室"
    getHtmlMain(city, channel, pages, room)
