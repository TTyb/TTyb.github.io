#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import execjs
import time
import random
import requests
import re
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


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


# 提取token的正则表达式
def get_token_re(token_response):
        reg = r'("token" : ")(.+?)(",)'
        all = re.compile(reg)
        alllist = re.findall(all, token_response)
        return alllist[0][1]

# 提取codestring的正则表达式
def get_codestring_re(codestring_html):
    reg = r'("codeString" : ")(.+?)(",)'
    all = re.compile(reg)
    alllist = re.findall(all, codestring_html)
    return alllist[0][1]

# 提取rsakey的正则表达式
def get_key_re(token_url):
    resp = gethtml(token_url)
    dict = {}
    data = json.loads(re.search(r'.*?\((.*)\)', resp.text).group(1).replace("'", '"'))

    dict["rsakey"] = data.get("key")
    dict["pubkey"] = data.get("pubkey")

    return dict

def post_cookie(postdata,dict):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
              'Host': 'passport.baidu.com',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
              'Cookie': dict["HOSUPPORT"] + "; " + dict["BAIDUID"] + "; " + dict["FG"],
              'Connection': 'keep-alive'}

    conn = requests.session()
    resp = conn.post('https://passport.baidu.com', headers=header, data=postdata)
    cookies = requests.utils.dict_from_cookiejar(conn.cookies)

    url = "https://www.baidu.com/"
    html = gethtml(url).content.decode("utf-8","ignore")
    print(html)


def encript_password(password, pubkey):
    cipher = PKCS1_v1_5.new(RSA.importKey(pubkey.encode('utf-8')))
    cipher_text = base64.b64encode(cipher.encrypt(password.encode('utf-8')))
    return cipher_text.decode('utf-8')

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

    # 获取callback
    callback = ctx.call("callback")
    # 获取gid
    gid = ctx.call("gid")
    # 获取tt
    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    tt = nowtime + timerandom

    # 获取token
    token_url = "https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt=" + str(tt) + "&class=login&gid=" + gid + "&logintype=dialogLogin&callback=" + callback
    # 获取set_cookie
    token_htmlbytes = gethtml(token_url)
    token_cookie = get_cookie(getset_cookie(token_htmlbytes))
    # 携带cookie得到token
    token_response = gethtml_cookie(token_url, token_cookie).content.decode("utf-8","ignore")
    token = get_token_re(token_response)

    # 获取codestring
    username = "灰色52056"
    dv = "MDEwAAoAKgAKAn8AGwAAAF00AA0CAB_Ly56rseWk6q3_vvOs86PwoP_HmMex1KbPqdCT_Jj9BwIABMvLy8sJAgAi3d9eXqWlpaWl8TMzZyZoL308cS5xIXIifUUaRTZDIUwlUQ0CAB_Ly-qhu--u4Kf1tPmm-an6qvXNks273qzFo9qZ9pL3DQIAHcvL6uH5reyi5bf2u-S767jot4_Qj_-e7Z7phvSQDQIAHcvL3ZCI3J3TlMaHypXKmsmZxv6h_ov4ne-hwK3IBwIABMvLy8sMAgAf09PT09PBLXk4djFjIm8wbz9sPGNbBFsuXThKBGUIbQcCAATLy8vLBwIABMvLy8sHAgAEy8vLyxMCABrL3d3dtcG1xbaMo4z7jPvVt9a_266A44zhzhACAAHLAQIABsvJycbPMAUCAATLy8vBFQIACMvLypa8Ce2SBAIABsjIysv4yhYCACLqnvXF69rs2eDX4tPn0uPS4NTn1-HQ5N3o2-3Y6dHj1ubUFwIACMrK3Nzf4sXiBgIAKMvLy6Ojo6Ojo6Om4-Pj4uvr6-64uLi7u7u7vujo6OoyMjI3UVFRU7sJAgAk09G4uJubm5ubmtvbj86Ax5XUmcaZyZrKla3yrdirzrzyk_6bBwIABMvLy8sMAgAf09PT09PbVABBD0gaWxZJFkYVRRoifSJXJEEzfRxxFAwCAB_T09PT08HksPG_-Krrpvmm9qX1qpLNkueU8YPNrMGkDAIAH9PT09PTwFQAQQ9IGlsWSRZGFUUaIn0iVyRBM30ccRQMAgAf09PT09PHqv6_8bbkpei36Ljru-Tcg9yp2r_Ng-KP6g0CAB3Ly91cRBBRH1gKSwZZBlYFVQoybTJCI1AjVDtJLQ"
    codestring_url = "https://passport.baidu.com/v2/api/?logincheck&token=" + token + "&tpl=mn&apiver=v3&tt=" + str(tt) + "&sub_source=leadsetpwd&username=" + username + "&isphone=false&dv=" + dv + "&callback=" + callback
    codestring_html = gethtml(codestring_url).content.decode("utf-8","ignore")
    codestring = get_codestring_re(codestring_html)

    # 获取rsakey
    raskey_url = "https://passport.baidu.com/v2/getpublickey?token=" + token + "&tpl=mn&apiver=v3&tt=" + str(tt) + "&gid=" + gid + "&callback=" + callback
    rsakeydict = get_key_re(raskey_url)
    rsakey = rsakeydict["rsakey"]
    pubkey = rsakeydict["pubkey"]
    # 获取password
    password = "tyb52056"

    enpasd=encript_password(password,pubkey)

    # 构造postdata
    postdata = {
        "apiver": "v3",
        "callback": callback,
        "charset": "UTF-8",
        "codestring": codestring,
        "countrycode": "",
        "crypttype": "12",
        "detect": "1",
        "dv": dv,
        "fp_uid": "8f29fdcf60e9b11186616c4baafa1509",
        "gid": gid,
        "idc": "",
        "isPhone": "",
        "logLoginType": "pc_loginDialog",
        "loginmerge": "true",
        "logintype": "dialogLogin",
        "mem_pass": "on",
        "password": password,
        "ppui_logintime": "26369",
        "quick_user": "0",
        "rsakey": rsakey,
        "safeflg": "0",
        "splogin": "rate",
        "staticpage": "https://www.baidu.com/cache/user/html/v3Jump.html",
        "subpro": "",
        "token": token,
        "tpl": "pp",
        "tt": tt,
        "u": "https://www.baidu.com/",
        "username": username
    }



    postdata1={
        "staticpage": "https://passport.baidu.com/static/passpc-account/html/v3Jump.html",
        "charset": "UTF-8",
        "token": token,
        "tpl": "pp",
        "subpro": "",
        "apiver": "v3",
        "tt": tt,
        "codestring": codestring,
        "safeflg": "0",
        "u": "https://passport.baidu.com/",
        "isPhone": "",
        "detect": "1",
        "gid": gid,
        "quick_user": "0",
        "logintype": "basicLogin",
        "logLoginType": "pc_loginBasic",
        "idc": "",
        "loginmerge": "true",
        "username": username,
        "password": enpasd,
        "mem_pass": "on",
        "rsakey": rsakey,
        "crypttype": "12",
        "ppui_logintime": "26369",
        "countrycode": "",
        "fp_uid": "d02c2d639771ae50b7e87f93069ace1e",
        "dv": "MDEwAAoAgAAKA4wAJAAAAF00AAkCACTT0BgZEBAQEBpzERFFBEoNXx5TDFMDUABfbDNsGWoPfTNSP1oIAgAJy8gsLenp6cHlCAIAKNTXe3odHR0CSR1cElUHRgtUC1sIWAc0azRZPFEzViR0FWYVWThaP1MNAgAdy8vRUEgcXRNUBkcKVQpaCVkGNWo1RSRXJFM8TioHAgAEy8vLywwCAB_TlZWVlY37r-6g57X0uea56brqtYbZhvOA5ZfZuNWwDAIAH9OXl5eXgSdzMnw7aShlOmU1ZjZpWgVaL1w5SwVkCWwHAgAEy8vLywwCAB_TgICAgJas-Ln3sOKj7rHuvu294tGO0aTXssCO74LnBwIABMvLy8sJAgAk09BiY21tbW1teTY2YiNtKng5dCt0JHcneEsUSz5NKFoUdRh9CAIACcvKi4mPj4-esQYCACjLy8uMjIyMjIyMiQYGBgdUVFRR8fHx8nZ2dnPT09PQjIyMiTk5OTpWFwIAFcjK9fXl2LbTpITniKCJssSl1_edoAUCAATLy8vBAQIABsvJycbPMBUCAAjLy8qWr5sJWgQCAAbIyMrL_8wWAgAi6p71xevc5dXg1-7Z6NDj0ufX5dHl1ODZ7Nrq0uHX4tTg0hACAAHLEwIAKMvv7--H84f3hL6Rvs6v3K_fsMK2mPqb8pbjza7BrIP1x-jXu9Sz2rQHAgAEy8vLywgCACHT0Hd2REREVovfntCXxYTJlsmZyprF9qn2hueU55D_jekNAgAdy8vfgprOj8GG1JXYh9iI24vU57jnkuGE9rjZtNEMAgAf05KSkpKE4rb3uf6s7aD_oPCj86yfwJ_qmfyOwKHMqQcCAATLy8vLBwIABMvLy8sMAgAf05KSkpKFXQlIBkETUh9AH08cTBMgfyBVJkMxfx5zFgkCACTT0E1Menp6enpgIyN3Nng_bSxhPmExYjJtXgFeLk88TzhXJUENAgAdy8vRobntrOKl97b7pPur-Kj3xJvEscKn1Zv6l_IJAgAi3d5oacjIyMjI7HFxJWQqbT9-M2wzYzBgPwxTDH8KaAVsGAcCAATLy8vLDQIAHcvL71RMGFkXUAJDDlEOXg1dAjFuMUEgUyBXOEouDQIAG8vL7y07by5gJ3U0eSZ5KXoqdUYZRjVAIk8mUggCAAnLyTk48_Pz2FgJAgAk09AYGRAQEBAacsPDl9aY343Mgd6B0YLSjb7hvsu43a_hgO2I",
        "callback": callback,
    }

    post_cookie(postdata1,token_cookie)
