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

    dv = "	MDExAAoAogALA44AJAAAAF00AAgCACOLiNbXsLCxIksfXhBXBUQJVglZCloFNmk2Wz5TMVQmdhdkFwwCAB-JmZmZmBNxJWQqbT9-M2wzYzBgPwxTDHkKbx1TMl86DAIAH4mJiYmIDhRAAU8IWhtWCVYGVQVaaTZpHG8KeDZXOl8IAgAJkZW2t97e31_ZCQIAJImKNjcyMjIyM1UbG08OQAdVFFkGWQlaClVmOWYTYAV3OVg1UAgCACGJilhZTU1NwvKm56nuvP2w77Dgs-O8j9CP-onsntCx3LkNAgAdkZGBnYXRkN6Zy4rHmMeXxJTL-Kf4jf6b6afGq84NAgAFkZGBj48NAgAFkZGaeHgMAgAfiZubm5uQ47f2uP-t7KH-ofGi8q2ewZ7rmP2PwaDNqBMCAFyRycnJodWh0aKYt5joifqJ-ZbkkL7cvdSwxeuI54ql0-HO8Z3ylfyStMH8lOCU5JeygLWGx-LQ5deRtIazgce31qXWpsm7z-GD4ovvmrTXuNXwwvfFg-CF65_6iAUCAASRkZGdAQIABpGTk4OO7hUCAAiRkZDP26GAkAQCAAaSkpCRopAWAgAisMSvn7GGsYG5jLWDsYS8iLCIvo6_jruLvISzhLSCu4u5gRcCABiQk7S0p_rS-8Cu9ZjotYnnvP2ew5j1mscQAgABkQYCACiRkZHW1tbW1tbW01xcXF2ampqfPz8_PLi4uL0dHR0eQkJCR_f39_SYBwIABJGRkZEJAgAkiYpkZWVlZWVlZc3NmdiW0YPCj9CP34zcg7DvsMW206HvjuOGBwIABJGRkZENAgAdkZGRU0sfXhBXBUQJVglZCloFNmk2QzBVJ2kIZQAHAgAEkZGRkQ0CAB2RkZpJUQVECk0fXhNME0MQQB8scyxZKk89cxJ_GgkCACSJilRVWVlZWVnXmJjMjcOE1pfahdqK2YnW5brlkOOG9LrbttMHAgAEkZGRkQkCAAyRkQgJGxsbGxp4rq4HAgAEkZGRkQgCAAmRkqSka2tqDsAJAgAkiYo-Pzk5OTk4usTEkNGf2IrLhtmG1oXVirnmucy_2qjmh-qPBwIABJGRkZEHAgAEkZGRkQwCAB-J7Ozs7WAnczJ8O2koZTplNWY2aVoFWi9cOUsFZAlsDAIAH4nr6-vqZGI2dzl-LG0gfyBwI3MsH0Afahl8DkAhTCkIAgAdhYHV1I-PjhUDVxZYH00MQR5BEUISTX4hfhh3BWg"
    # fp_info = "	25dc4e90f115ed0abe95320051d9bf8c002~~~~zyH0Qgd5Sc_g~~JwyF5BYh5mLx5Zo_yyF5BYh5mL-2~o_Q~eLrX~eLrL~~rS~~CAy0UrYzbPAm0A8Exm8EbdDzglYMrtIvg~JMCPIQ-jINrx8ExsAEnwAMCgJsYdAvWH1bbQIQCBDvbKApUOAm0HABPdGb2RJMngBEew8EWg1zCHIaWC8zew6ExSAMnh7zxtpMAOAqgdGQ0K8axwIvtHEm0dBv0PpvWUAQgd7zxtum0dIv0P56-t1~od5yxwIvtHEm0dBv0P0M2gGgrH8E8PI~PdGmlH8M2gG~cd5a-K1~5dAvWH1bCgIz2gINCCpBPdGvb~8vgQAMLdAvWH1bCgIz2gINCBpheYIvbhAzeKIBPdGb2BBhb-YsCKIqAOGgrpBveNDE-dAvWH1bbCtx1Z457otxIaHH9gtF3ZlG9Vtx~aO57T7zxtpMPOIz028M2PJKxwIvtHp0bmJEUgpvWUAQgdpmnO7zxtGMbsAEnNJEUg1zCHIaWZBw4nYhb9Y0lYIm0NDE-jINr~JEPluaxwIvtHYhx16M2xGQgdAzeYIm0NDE-jINrSuM2PIzAO1zCHIaWCppUPIzgqBbrH8E8PI~PdGblvBEgdDpC5pvWUAQgd1zCHIaW2DE2KIs2OANCXAzAPJQpK5ZqS7wxYpUrMpwbY1wC5BaWdGbbCpvlO8veqGzbsCMLjINrCp0rRIsCOCmnl8h0-1zCHIaWCppUlDEWYIm0NDE-jINrCppUlDEWMAEn1DMYdAvWH1bCgIz2gINCv0qxtIm0N1Egd7zxt8mlz8vxMAEn1DMYdAvWH1qbwIQngYE2KIQnl8ZPdGmrwA~5K1zCHIaWrAveyApb~GzeyJMYjINrtAvJS5yxwIvtHYECOJz0rYpUqAMCgJsYjINrrAveyApbrBpCg8v0~8Z5K1zCHIo__xg~oCg~oWg~oGg~rMy0jIpMAOAqgdGQ0K8aWdGbe-8ExHAEg3GvWUAQgd1qC5BaWpEb2BBKWpDvgSGvWUAKUPIzgS8mnlIN2zAMnSIQACuzedApUUGQg~8QlgIzetAExPIz8CuzedAEgdJM8gJNrlAQ0sDMCRCzgKAEAOua-Hp0bMAEnmJEUgpvWUAQgdpmnO1vxtJQbfJMLHINrSuM2PIzAO1vxtEqAYIm0N1b2RJMngpvePINCYIm0N1EgdAzeKCzgKAEAOuaWCppUlDEWYIm0NDExzIsnsAEnFDMYHp0b2JEgHpvWUAQgdAzeK8Q0yDQgh1vxt8mlz8v-HYE2KIQnl8brOGNClJzWgCve~8EUgINCvIsn4JMYHYECOJz0YCqAPIgl2BqAOGzUl8aWrAveyA0rqCzgdEqU5CzeKIEbh1qb~GzeyJMCvIsn4GhCl8vbvIsn4JMYHEqU50z0KGQgOIzezYE2KIQnl8qAOGzUSCvbhJpAOGzUl8aWrJsnOJzbhEqU5CvbhJ0rlJQ4lAQpHYECOJz0vIsn4CzWO8SwxCvbhJpAPIvpHYE2KIQnl8brOGNClJzWgCve~8EUgINCvIsn4JMYHYECOJz0YCqAPIgl2BqAOGzUl8aWrAveyA0rqCzgdEqU5CzeKIEbh1qb~GzeyJMCvIsn4GhCl8vbvIsn4JMYHEqU50z0KGQgOIzezYE2KIQnl8qAOGzUSCvbhJpAOGzUl8aWrJsnOJzbhEqU5CvbhJ0rlJQ4lAQpHYECOJz0vIsn4CzWO8SwxCvbhJpAPIvpHYECOJz0rYpUqAMCgJsY_B-0R~atqGl4ZZo5woqyBk4FmoqjqNVEY4M-LcxoRrOYR69LqtL7vpDj2-eQYsV37hjVbrBvhATooo69mKn-JWLLnw3g5ohixrg~rOg~r-g~rFg~rN~~cIyHuzL4Yh-_Hys8ExSGv0~DEAPAEY_~g~re~tLAdmaZs~~oag~of~vVvA99Eg~oRg~obg~odg~ohyT1BYd7BLs5BLS7ZoS5SGW5ZcU"
    # fp_uid = "25dc4e90f115ed0abe95320051d9bf8c"
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
        "u": "https://passport.baidu.com/center",
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
        # "traceid":57308501,
        # "fp_info":fp_info,
        # "fp_uid":fp_uid,
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
    username = "灰色52056"
    password = "tyb52056"
    login(username, password)
    home_page = session.get("https://passport.baidu.com/center", headers=headers).content.decode("utf-8", "ignore")
    print(home_page)

    # json_file = open("cookie.json")
    # cookies = json.load(json_file)
    # json_file.close()
    #
    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
    #           'Host': 'passport.baidu.com',
    #           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #           'Accept-Encoding': 'gzip, deflate',
    #           'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    #           'Connection': 'keep-alive'}
    #
    # home_page = requests.get("https://passport.baidu.com/center", headers=headers,cookies=cookies).content.decode("utf-8", "ignore")
    # print(home_page)