#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import execjs
import time
import random
import requests


# get网页的函数，没有cookie
def gethtml(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
              'Host': 'passport.baidu.com',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
              'Connection': 'keep-alive'}

    # 解析网页
    html_bytes = requests.get(url, headers=header)
    return html_bytes


# 携带cookie的get网页的函数
def gethtml_cookie(url, dict):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
              'Host': 'passport.baidu.com',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
              'Cookie': dict["HOSUPPORT"] + "; " + dict["BAIDUID"] + "; " + dict["FG"],
              'Connection': 'keep-alive'}

    # 解析网页
    html_bytes = requests.get(url, headers=header)
    return html_bytes


# 获取返回头部的set-cookie
def getset_cookie(response):
    return response.headers['set-cookie']


# 解析set-cookie获得cookie的字典
def get_cookie(setcookie):
    dict = {}
    temparr = setcookie.split(" ")
    for item in temparr:
        if "HOSUPPORT" in item:
            dict["HOSUPPORT"] = item
        elif "FG" in item:
            for itm in item.split(":"):
                if "FG" in itm:
                    dict["FG"] = itm
                if "BAIDUID" in itm:
                    dict["BAIDUID"] = itm
    return dict


#

if __name__ == '__main__':
    js = '''function callback(){
            return 'bd__cbs__'+Math.floor(2147483648 * Math.random()).toString(36)
        }
        function gid(){
            return 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (e) {
            var t = 16 * Math.random() | 0,
            n = 'x' == e ? t : 3 & t | 8;
            return n.toString(16)
            }).toUpperCase()
        }'''
    ctx = execjs.compile(js)

    callback = ctx.call("callback")
    gid = ctx.call("gid")

    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    tt = nowtime + timerandom

    token_url = "https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt=" + str(tt) + "&class=login&gid=" + gid + "&logintype=dialogLogin&callback=" + callback
    print(token_url)
    token_htmlbytes = gethtml(token_url)
    token_cookie = get_cookie(getset_cookie(token_htmlbytes))
    token_response = gethtml_cookie(token_url, token_cookie).content.decode("utf-8","ignore")
    print(token_response)

    postdata = {
        "apiver": "v3",
        "callback": callback,
        "charset": "UTF-8",
        "codestring": "njG4306e29ac00fe26d02d914aade01b5142ed8de066f041367",
        "countrycode": "",
        "crypttype": "12",
        "detect": "1",
        "dv": "MDEwAAoAKgAKAn8AGwAAAF00AA0CAB_Ly56rseWk6q3_vvOs86PwoP_HmMex1KbPqdCT_Jj9BwIABMvLy8sJAgAi3d9eXqWlpaWl8TMzZyZoL308cS5xIXIifUUaRTZDIUwlUQ0CAB_Ly-qhu--u4Kf1tPmm-an6qvXNks273qzFo9qZ9pL3DQIAHcvL6uH5reyi5bf2u-S767jot4_Qj_-e7Z7phvSQDQIAHcvL3ZCI3J3TlMaHypXKmsmZxv6h_ov4ne-hwK3IBwIABMvLy8sMAgAf09PT09PBLXk4djFjIm8wbz9sPGNbBFsuXThKBGUIbQcCAATLy8vLBwIABMvLy8sHAgAEy8vLyxMCABrL3d3dtcG1xbaMo4z7jPvVt9a_266A44zhzhACAAHLAQIABsvJycbPMAUCAATLy8vBFQIACMvLypa8Ce2SBAIABsjIysv4yhYCACLqnvXF69rs2eDX4tPn0uPS4NTn1-HQ5N3o2-3Y6dHj1ubUFwIACMrK3Nzf4sXiBgIAKMvLy6Ojo6Ojo6Om4-Pj4uvr6-64uLi7u7u7vujo6OoyMjI3UVFRU7sJAgAk09G4uJubm5ubmtvbj86Ax5XUmcaZyZrKla3yrdirzrzyk_6bBwIABMvLy8sMAgAf09PT09PbVABBD0gaWxZJFkYVRRoifSJXJEEzfRxxFAwCAB_T09PT08HksPG_-Krrpvmm9qX1qpLNkueU8YPNrMGkDAIAH9PT09PTwFQAQQ9IGlsWSRZGFUUaIn0iVyRBM30ccRQMAgAf09PT09PHqv6_8bbkpei36Ljru-Tcg9yp2r_Ng-KP6g0CAB3Ly91cRBBRH1gKSwZZBlYFVQoybTJCI1AjVDtJLQ",
        "fp_uid": "8f29fdcf60e9b11186616c4baafa1509",
        "gid": gid,
        "idc": "",
        "isPhone": "",
        "logLoginType": "pc_loginDialog",
        "loginmerge": "true",
        "logintype": "dialogLogin",
        "mem_pass": "on",
        "password": "",
        "ppui_logintime": "26369",
        "quick_user": "0",
        "rsakey": "ny7OwldzjXJw4RRLtoVmUcMqHq7c1GEt",
        "safeflg": "0",
        "splogin": "rate",
        "staticpage": "https://www.baidu.com/cache/user/html/v3Jump.html",
        "subpro": "",
        "token": "",
        "tpl": "mn",
        "tt": tt,
        "u": "https://www.baidu.com/",
        "username": "灰色52056",
        "verifycode": "成分"
    }
