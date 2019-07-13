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
    }
    function traceid(){
    var e = {a: 1, b: 1, c: 1}
    e.traceID = {
            headID: e.traceID && e.traceID.headID || "",
            flowID: e.traceID && e.traceID.flowID || "",
            cases: e.traceID && e.traceID.cases || "",
            initTraceID: function(e) {
                var t = this;
                e && e.length > 0 ? (t.headID = e.slice(0, 6),
                t.flowID = e.slice(6, 8)) : t.destory()
            },
            createTraceID: function() {
                var e = this;
                return e.headID + e.flowID + e.cases
            },
            startFlow: function(e) {
                var t = this
                  , n = t.getFlowID(e);
                0 === t.flowID.length || t.flowID === n ? (t.createHeadID(),
                t.flowID = n) : t.finishFlow(n)
            },
            finishFlow: function() {
                var e = this;
                e.destory()
            },
            getRandom: function() {
                return parseInt(90 * Math.random() + 10, 10)
            },
            createHeadID: function() {
                var e = this
                  , t = (new Date).getTime() + e.getRandom().toString()
                  , n = Number(t).toString(16)
                  , i = n.length
                  , s = n.slice(i - 6, i).toUpperCase();
                e.headID = s
            },
            getTraceID: function(e) {
                var t = this
                  , n = e && e.traceid || "";
                t.initTraceID(n)
            },
            getFlowID: function(e) {
                var t = {
                    login: "01",
                    reg: "02"
                };
                return t[e]
            },
            setData: function(e) {
                var t = this;
                return e.data ? e.data.traceid = t.createTraceID() : e.url = e.url + (e.url.indexOf("?") > -1 ? "&" : "?") + "traceid=" + t.createTraceID(),
                e
            },
            destory: function() {
                var e = this;
                e.headID = "",
                e.flowID = ""
            }
        };
        e.traceID.initTraceID()
        e.traceID.createHeadID()

        return e.traceID.createTraceID()+"01"
    }"""
ctx = execjs.compile(js)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"}

session = requests.session()
session.get("https://passport.baidu.com/v2/?login", headers=headers)

def get_tk_as_ds():
    resp=session.get(url="https://passport.baidu.com/viewlog?ak=1e3f2dd1c81f2075171a547893391274&as=74a154e4&fs=MEBGsUNpNVBMjs8Tdudr8aAjW%2BFklVpfnDnMkmxZ3DMXZisUPveYoxrXH2HKd5pgidlfhvibzXjlMLk28ZUvrUpDazz2aivj1lT0DHKRrMLZBBvYrMBdY%2BenNlaoF8h%2F8s18t0DQtONJZoRMOt%2FDotooaXA1bPuODU3XkP5iOBv9GpK6mApUn2xQXIpSEFTInDKJEiFBfC04IfPyCVCe766QJT%2FS4CHeqIJsjVLa7aoNnh3%2BHSdvRx1Uay1Fy60q%2Fkz5TJ%2B8Ib25o8yDfFBcOdbIdhVwmDHp3R87v3%2BY0M9rl2MUlr4ZJO2vn98yspz9t60LrqhUsObz7FZIdG9sWRP6JNt00%2BeQIY6Z7liRZI75mSRTWGDHYMT8LU7KdOELrxdrM7OfHfoD%2BlJ8PpCPFPT8dOgJUKGwa0tkL6t5UKpOUUXoxbx3lkRUNSj5NxdNcRt3YZbDShJmXnRbfza7yDpgvzKBRULis%2BzxhbBijS5onMCPOB59OVGE6lges8nr9xhi0ZNM9f96V7S4elo4fsXUgQzmJJwsM69ah0RSVNFQbBNoGszbT47%2BHDORP%2Fd7OLGOeG8D9i5tMIf%2BYRgN6ing5B5lLpn5nn3KtshIWiAwrR5mijWZai7uheFiE2cHCovVBRAlfCp3yDtKRWN4cE55F9b0wvoDHSJmHqlVKp1%2BgbE9b1oUFmqOGWcWMakVQfrEFg6phufPuuaQLLdtX3%2Bir7yeC8rx8tHdcTz6CtJsWtVcavFV8Q8j8Ta90bSKp%2BjQlmOXmct7PeM3tRM8%2B946o67jwNX7CP1EjKw%2FYk5lP%2BmCqNjwK3eZf46pQGLmZYUOLuGBK73HeCPAlj4YlEfGrZYpCuLp1vthWK%2B5oZZR9c%2BLpu1aOGotEqebe2N6UaKbXhC2qn6h3glylAV%2B2HfY4wut%2Bj%2Frr3iJEhWLj7J7qD0fr5ojR993ru8qrZSxKYu1f5W6NhdGPz7ZpWRfBrIaxtMjliEgdrIZ82RSe930OeXJaXMzytvoxvsZaUYvODivXMsPXDlnEQ%2FiZPPAO1B3F06Y8so67piru9hrXdkBwGLP6G07wo2dCMPvSFHHuLSvFYWduRFscftm3qJ1XUSDHDYIe8t5y5ClLJJd%2FCAkdlhQc3iOQJUgOXp4tAjoSkkiLnramq%2BIa6ycbi%2BcfzE6recOWVsuTFC4rX0t4RLdY5yf%2BRkED6qYcR8LLorK0dVKTX34rRsvLFElzgbi%2FW1%2Fq8y8tU9X%2F3pQXzHEsw28si6pjHvbPd4rJoQTIoI5asbCbxKqjRCJCfJPXRbUxo%2BZeWwik4F5UiTzwpas3pQ%3D&callback=jsonpCallbackb5819&v=4646", headers=headers)
    start = resp.text.find('(')
    data = (json.loads(resp.text[start + 1:-1]))['data']
    tk = data.get('tk')
    _as = data.get('as')
    ds = data.get('ds')
    return tk,_as,ds


def get_gid():
    return ctx.call("gid")


def get_callback():
    return ctx.call("callback")


def get_traceid():
    return ctx.call("traceid")

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
    tk, _as, ds=get_tk_as_ds()
    gid = get_gid()
    callback = get_callback()
    traceid=get_traceid()
    token = get_token(gid, callback)
    dicts = get_rsakey(token, gid, callback)
    tt = get_tt()
    rsakey = dicts["rsakey"]
    pubkey = dicts["pubkey"]
    newpassword = base64_password(password, pubkey)

    dv = "tk0.084246779043189111563000601025@eer0rCvG6wAkqBQHKBQm~O4kFUTk2-AkqBK2u85UshGKyTJu4n9w4T9ZKwD9s8FrU3Ak6Ov17UTk2-AkqBK2u85UshGKyTJu4n9w4T9ZKwD9s8FrU3Ak6w8GVUTkJwAkqBK2u85UshGKyTJu4n9w4T9ZKwD9s8FrU3Ak6b8kVZTkJ~AkqBK2u85UshGKyTJu4n9w4T9ZKwD9s8FrU3Ak6b8GNZTq__vr0PevG2bvm~w41nB4kq-8CjxvG2~vE~UvkNB4kVw8Cjx4w7wAkFjvE~-4k6ZAo~jvGnXAk6U8C~fvGqbAu5hGVRCnJUT9UhGJuxw9UyUN-KOGauiD9~j4wV-Ak6O4O~jvk2w8mjxCttPwt-Dx9tRh-rivC~wAkvOyrqR0B~A1qf4k6b41NZ8Gqbvw2f8G2jvGJ-vwq~vkF~vGqO4n__ir0~tPo5bNovdAOy~F94wN0yORmXEFr3VRCX1Q-bcR16cp-jcD-3IAoKID0KaPrX3Dq__Irl4w2Bvm~j8GqwAkV-8C~j8G6~Ak2~8kqBvGVOvm~j8Gv-Ak2~4GF_"

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
        "u": "https://passport.baidu.com/",
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
        "fp_uid": "",
        "fp_info": "",
        "loginversion": "v4",
        "ds": ds,
        "tk": tk,
        "dv": dv,
        "traceid":traceid,
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
    username = "你的账号"
    password = "你的密码"
    login(username, password)
    home_page = session.get("https://passport.baidu.com/center", headers=headers).content.decode("utf-8", "ignore")
    
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
