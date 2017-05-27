#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import execjs
import time
import random
import requests
import re
import json
import rsa
import base64

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
           'Host': 'passport.baidu.com',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
           'Connection': 'keep-alive'}

# 全局的session
session = requests.session()
session.get('https://passport.baidu.com/v2/?login', headers=headers)

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


def get_gid(ctx):
    return ctx.call('gid')


def get_callback(ctx):
    return ctx.call('callback')


def get_tt():
    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    tt = str(nowtime) + str(timerandom)

    return tt


def get_token(gid, callback):
    tt = get_tt()
    get_data = {
        'tpl': 'pp',
        'subpro': 'netdisk_web',
        'apiver': 'v3',
        'tt': tt,
        'class': 'login',
        'gid': gid,
        'logintype': 'basicLogin',
        'callback': callback
    }
    resp = session.get(url='https://passport.baidu.com/v2/api/?getapi', params=get_data, headers=headers)
    if resp.status_code == 200 and callback in resp.text:
        data = json.loads(re.search(r'.*?\((.*)\)', resp.text).group(1).replace("'", '"'))
        return data.get('data').get('token')
    else:
        print('获取token失败')
        return None


def get_key(token, gid, callback):
    tt = get_tt()
    raskey_url = "https://passport.baidu.com/v2/getpublickey?token=" + token + "&tpl=pp&apiver=v3&tt=" + str(
        tt) + "&gid=" + gid + "&callback=" + callback
    resp = gethtml(raskey_url)
    dict = {}
    data = json.loads(re.search(r'.*?\((.*)\)', resp.text).group(1).replace("'", '"'))

    dict["rsakey"] = data.get("key")
    dict["pubkey"] = data.get("pubkey")

    return dict


def encript_password(password, pubkey):
    pub = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode('utf-8'))
    encript_passwd = rsa.encrypt(password.encode('utf-8'), pub)
    return base64.b64encode(encript_passwd).decode('utf-8')


# get网页的函数，没有cookie
def gethtml(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
              'Host': 'passport.baidu.com',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
              'Connection': 'keep-alive'}

    # 解析网页
    html_bytes = session.get(url, headers=header)
    return html_bytes



def post_cookie(postdata):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
              'Host': 'passport.baidu.com',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
              'Referer': 'https://passport.baidu.com/v2/?login',
              'Connection': 'keep-alive'}

    resp = session.post('https://passport.baidu.com/v2/?login', headers=headers, data=postdata)

    print("resp.text",resp.text)

    if 'err_no=0' in resp.text:
        print('登录成功')
    else:
        print('登录失败')

    cookie = requests.utils.dict_from_cookiejar(session.cookies)

    home_page = session.get("https://passport.baidu.com/center", headers=header).content.decode("utf-8", "ignore")
    print(home_page)
    # print(html)


if __name__ == '__main__':
    gid = get_gid(ctx)
    callback = get_callback(ctx)
    tt = get_tt()
    token = get_token(gid, callback)
    dict = get_key(token, gid, callback)
    rsakey = dict["rsakey"]
    pubkey = dict["pubkey"]

    print("gid=", gid)
    print("callback=", callback)
    print("tt=", tt)
    print("token=", token)
    print("rsakey=", rsakey)
    print("pubkey=", pubkey)

    username = "灰色52056"
    dv = "MDEwAAoA3AAKAskAIAAAAF00AAcCAATLy8vLCQIAIt3edHXh4eHh4SNXVwNCDEsZWBVKFUUWRhkqdSpZLE4jSj4IAgAJy8mTk1tbW-WZCAIACcvJubutra0abg0CAB3Ly27s9KDhr-i6-7bptua15bqJ1on8j-qY1rfavwwCAB_Ttra2thQAVBVbHE4PQh1CEkERTn0ifQh7HmwiQy5LDAIAH9PDw8PDYz5qK2UicDF8I3wsfy9wQxxDNkUgUhx9EHUHAgAEy8vLywwCAB_TwsLCwluz56bor_288a7xofKi_c6RzrvIrd-R8J34DQIAHcvLWUpSBkcJThxdEE8QQBNDHC9wL1opTD5wEXwZBwIABMvLy8sJAgAk09AWFurq6urqe4uL357Ql8WEyZbJmcqaxfap9oPwleepyKXACAIAHd_ceHlRUVHBRxNSHFsJSAVaBVUGVgk6ZTpcM0EsBwIABMvLy8sGAgAoy8vLjIyMjIyMjIkGBgYFEBAQFbW1tbYyMjI3l5eXlMjIyM19fX1-EhMCACjL7-_vh_OH94S-kb7Or9yv37DCtpj6m_KW482uwayD9cfo17vUs9q0FwIADMvLsrK1krvmz7TRpwQCAAbIyMrL_8wVAgAIy8vKlqwQ8A8BAgAGy8nJxs8wBQIABMvLy8EWAgAj6Z32xujb7djv3era4tPk1-7a7dnu2ejc5dDm1eHR5tPr0uYQAgAByw0CAAXLy8x6eg0CAAXLy1lXVwcCAATLy8vLDAIAH9PDwsLCWHsvbiBnNXQ5ZjlpOmo1BlkGcwBlF1k4VTAMAgAf09PT09NIfiprJWIwcTxjPGw_bzADXAN2BWASXD1QNQcCAATLy8vLDQIAHcvLbvzksPG_-Krrpvmm9qX1qpnGmemI-4j_kOKGCAIACcvIPz6JiYk5pQgCAB_d3nh57e3tLI3ZmNaRw4LPkM-fzJzD8K_wg_aU-ZDk"
    password = encript_password("tyb52056", pubkey)

    # 构造postdata
    postdata = {
        "staticpage": "https://passport.baidu.com/static/passpc-account/html/v3Jump.html",
        "charset": "UTF-8",
        "token": token,
        "tpl": "pp",
        "subpro": "",
        "apiver": "v3",
        "tt": tt,
        "codestring": "",
        "safeflg": 0,
        "u": "https://passport.baidu.com/",
        "isPhone": "",
        "detect": 1,
        "gid": gid,
        "quick_user": 0,
        "logintype": "basicLogin",
        "logLoginType": "pc_loginBasic",
        "idc": "",
        "loginmerge": "true",
        "username": username,
        "password": password,
        "mem_pass": "on",
        "rsakey": rsakey,
        "crypttype": 12,
        "ppui_logintime": 26369,
        "countrycode": "",
        "fp_uid": "d02c2d639771ae50b7e87f93069ace1e",
        "dv": dv,
        "callback": 'parent.' + callback,
    }

    post_cookie(postdata)
