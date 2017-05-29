import time
import json
import re
import requests
import execjs
import rsa
import base64
import random

js = """function callback(){
        return "bd__cbs__"+Math.floor(2147483648 * Math.random()).toString(36)
    }
    function gid(){
        return "xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (e) {
        var t = 16 * Math.random() | 0,
        n = "x" == e ? t : 3 & t | 8;
        return n.toString(16)
        }).toUpperCase()
    }"""
ctx = execjs.compile(js)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"}

session = requests.session()
session.get("https://passport.baidu.com/v2/?login", headers=headers)


def get_gid():
    return ctx.call("gid")


def get_callback():
    return ctx.call("callback")


def get_tt():
    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    tt = str(nowtime) + str(timerandom)
    return tt


def get_token(gid, callback):
    tt = get_tt()
    tokendata = {
        "tpl": "pp",
        "subpro": "",
        "apiver": "v3",
        "tt": tt,
        "class": "login",
        "gid": gid,
        "logintype": "basicLogin",
        "callback": callback
    }
    headers.update(
        dict(Referer="http://passport.baidu.com/", Accept="*/*", Connection="keep-alive", Host="passport.baidu.com"))
    resp = session.get(url="https://passport.baidu.com/v2/api/?getapi", params=tokendata, headers=headers)

    data = json.loads(re.search(r".*?\((.*)\)", resp.text).group(1).replace("'", '"'))
    token = data.get('data').get('token')
    return token


def get_rsakey(token, gid, callback):
    tt = get_tt()
    rsakeydata = {
        "token": token,
        "tpl": "pp",
        "subpro": "",
        "apiver": "v3",
        "tt": tt,
        "gid": gid,
        "callback": callback,
    }
    resp = session.get(url="https://passport.baidu.com/v2/getpublickey", headers=headers, params=rsakeydata)
    data = json.loads(re.search(r".*?\((.*)\)", resp.text).group(1).replace("'", '"'))

    dicts = {}
    dicts["rsakey"] = data.get("key")
    dicts["pubkey"] = data.get("pubkey")
    return dicts


def base64_password(password, pubkey):
    pub = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode("utf-8"))
    encript_passwd = rsa.encrypt(password.encode("utf-8"), pub)
    return base64.b64encode(encript_passwd).decode("utf-8")


def login(username, password):
    gid = get_gid()
    callback = get_callback()
    token = get_token(gid, callback)
    dicts = get_rsakey(token, gid, callback)
    tt = get_tt()
    rsakey = dicts["rsakey"]
    pubkey = dicts["pubkey"]
    newpassword = base64_password(password, pubkey)

    dv = "MDEwAAoA3AAKAskAIAAAAF00AAcCAATLy8vLCQIAIt3edHXh4eHh4SNXVwNCDEsZWBVKFUUWRhkqdSpZLE4jSj4IAgAJy8mTk1tbW-WZCAIACcvJubutra0abg0CAB3Ly27s9KDhr-i6-7bptua15bqJ1on8j-qY1rfavwwCAB_Ttra2thQAVBVbHE4PQh1CEkERTn0ifQh7HmwiQy5LDAIAH9PDw8PDYz5qK2UicDF8I3wsfy9wQxxDNkUgUhx9EHUHAgAEy8vLywwCAB_TwsLCwluz56bor_288a7xofKi_c6RzrvIrd-R8J34DQIAHcvLWUpSBkcJThxdEE8QQBNDHC9wL1opTD5wEXwZBwIABMvLy8sJAgAk09AWFurq6urqe4uL357Ql8WEyZbJmcqaxfap9oPwleepyKXACAIAHd_ceHlRUVHBRxNSHFsJSAVaBVUGVgk6ZTpcM0EsBwIABMvLy8sGAgAoy8vLjIyMjIyMjIkGBgYFEBAQFbW1tbYyMjI3l5eXlMjIyM19fX1-EhMCACjL7-_vh_OH94S-kb7Or9yv37DCtpj6m_KW482uwayD9cfo17vUs9q0FwIADMvLsrK1krvmz7TRpwQCAAbIyMrL_8wVAgAIy8vKlqwQ8A8BAgAGy8nJxs8wBQIABMvLy8EWAgAj6Z32xujb7djv3era4tPk1-7a7dnu2ejc5dDm1eHR5tPr0uYQAgAByw0CAAXLy8x6eg0CAAXLy1lXVwcCAATLy8vLDAIAH9PDwsLCWHsvbiBnNXQ5ZjlpOmo1BlkGcwBlF1k4VTAMAgAf09PT09NIfiprJWIwcTxjPGw_bzADXAN2BWASXD1QNQcCAATLy8vLDQIAHcvLbvzksPG_-Krrpvmm9qX1qpnGmemI-4j_kOKGCAIACcvIPz6JiYk5pQgCAB_d3nh57e3tLI3ZmNaRw4LPkM-fzJzD8K_wg_aU-ZDk"

    post_data = {
        "staticpage": "https://passport.baidu.com/static/passpc-account/html/v3Jump.html",
        "charset": "utf-8",
        "token": token,
        "tpl": "pp",
        "subpro": "",
        "apiver": "v3",
        "tt": tt,
        "codestring": "",
        "safeflg": 0,
        "u": "http://passport.baidu.com/disk/home",
        "isPhone": "",
        "detect": 1,
        "gid": gid,
        "quick_user": 0,
        "logintype": "basicLogin",
        "logLoginType": "pc_loginBasic",
        "idc": "",
        "loginmerge": "true",
        "foreignusername": "",
        "username": username,
        "password": newpassword,
        "mem_pass": "on",
        "rsakey": rsakey,
        "crypttype": 12,
        "ppui_logintime": 33554,
        "countrycode": "",
        "dv": dv,
        "callback": "parent." + callback
    }
    resp = session.post(url="https://passport.baidu.com/v2/api/?login", data=post_data, headers=headers)
    if username in resp.content.decode("utf-8", "ignore"):
        print("登陆成功")
    else:
        print("登陆失败")

    cookies = requests.utils.dict_from_cookiejar(session.cookies)
    print(cookies)

    file = open("cookie.json","w")
    file.write(json.dumps(cookies))
    file.close()

if __name__ == "__main__":
    username = "username"
    password = "password"
    #login(username, password)
    #home_page = session.get("https://passport.baidu.com/center", headers=headers).content.decode("utf-8", "ignore")
    #print(home_page)

    json_file = open("cookie.json")
    cookies = json.load(json_file)
    json_file.close()

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
              'Host': 'passport.baidu.com',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
              'Connection': 'keep-alive'}

    home_page = requests.get("https://passport.baidu.com/center", headers=headers,cookies=cookies).content.decode("utf-8", "ignore")
    print(home_page)