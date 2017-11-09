#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from py.tbtmGoods.tbtmGoods import *

jsonPath = "json/" + time.strftime('%Y%m%d', time.localtime(time.time()))


def getfilename(filename):
    for root, dirs, files in os.walk(filename):
        array = files
        if array:
            return array


def readJson():
    list = []
    array = getfilename(jsonPath)
    for jn in array:
        jnPh = jsonPath + "/" + jn
        file = open(jnPh, "rb")
        infoList = json.loads(file.read().decode("utf-8", "ignore"))
        dictList = formatDict(1, infoList["listItem"])
        list = list + dictList
    return list


try:
    dictList = readJson().reverse()
except:
    dictList = [
        {"店名": "", "标题": "", "原价": "", "折扣价": "", "地址": "", "评论": "", "销量": "", "卖点": "", "优惠": "", "图像URL": ""}]

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template("home.html", dictList=dictList)
    elif request.method == 'POST':
        search = request.form["search"]
        page = int(request.form["page"])
        if search and page:
            getJsonData(page, search)
            newList = readJson().reverse()
            return render_template("home.html", dictList=newList)
        else:
            return render_template("home.html", dictList=dictList)


if __name__ == "__main__":
    app.run()
