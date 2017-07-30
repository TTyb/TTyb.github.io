#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import redis
from rediscluster import StrictRedisCluster

redis_nodes = [{'host': '192.168.230.218', 'port': 6380},
               {'host': '192.168.230.218', 'port': 6381},
               {'host': '192.168.230.218', 'port': 6382},
               {'host': '192.168.230.223', 'port': 6383},
               {'host': '192.168.230.223', 'port': 6384},
               {'host': '192.168.230.223', 'port': 6385}
               ]

r = StrictRedisCluster(startup_nodes=redis_nodes)

r.flushdb()

# 增加url到redis里面
def pushToRedis(name, valueList):
    for i in range(50):
        for item in valueList:
            r.lpush(name, item)

name = "url"
urlList = ["https://www.baidu.com", "http://www.tybai.com/"]
# 添加到消息列队中
pushToRedis(name, urlList)

