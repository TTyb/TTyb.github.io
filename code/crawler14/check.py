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

name = "url"

length = r.llen(name)
print(length)
print(r.lrange(name, 0, -1))
