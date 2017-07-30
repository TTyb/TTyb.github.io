import requests
import socket
import time
from rediscluster import StrictRedisCluster

session = requests.session()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"}


redis_nodes = [{'host': '192.168.230.218', 'port': 6380},
               {'host': '192.168.230.218', 'port': 6381},
               {'host': '192.168.230.218', 'port': 6382},
               {'host': '192.168.230.223', 'port': 6383},
               {'host': '192.168.230.223', 'port': 6384},
               {'host': '192.168.230.223', 'port': 6385}
               ]

r = StrictRedisCluster(startup_nodes=redis_nodes)

# 从redis中拿到url
def popFromRedis(name):
    return r.rpop(name).decode()


def getHtml(url):
    # 修饰头部
    headers.update(dict(Referer=url))
    # 抓取网页
    resp = session.get(url=url, headers=headers)
    return resp.content.decode("utf-8", "ignore")


# 保存到本地
def saveToLocal(html):
    hostname = socket.gethostname()
    ipName = ("2" + socket.gethostbyname(hostname) + "#" + str(time.time())).replace(".", "_")
    with open("/home/ttyb/html/" + ipName, "w") as fle:
        fle.write(html)
        fle.close()


def main():
    name = "url"
    length = r.llen(name)
    for i in range(length):
        url = popFromRedis(name)
        print(url)
        html = getHtml(url)
        saveToLocal(html)
        time.sleep(1)


if __name__ == "__main__":
    time.sleep(10)
    main()
