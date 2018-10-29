---
layout: post
categories: [python]
title: python3的socket使用
date: 2018-10-29
author: TTyb
desc: "需要实现两台机器的信息交互，使用 `socket` 进行调度"
---

如果需要设置两台机器的端口，请查看博文 [centos7开放端口和防火墙设置](http://www.tybai.com/linux/centos7%E5%BC%80%E6%94%BE%E7%AB%AF%E5%8F%A3%E5%92%8C%E9%98%B2%E7%81%AB%E5%A2%99%E8%AE%BE%E7%BD%AE.html)

需要实现两台机器的信息交互，使用 `socket` 进行调度。其中服务端为：

~~~ruby
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

# 服务端ip
server_address = ('192.168.229.129',10000)
# 客户端ip
client_address = ("192.168.229.130",10000)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(server_address)
while 1:
    data,addr=s.recvfrom(2048)
    if not data:
        break
    print("got data from",addr)
    print(data.decode())
    replydata = input("reply:")
    s.sendto(replydata.encode("utf-8"),client_address)
s.close()
~~~

客户端为：

~~~ruby
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

# 服务端ip
server_address = ('192.168.229.129',10000)
# 客户端ip
client_address = ("192.168.229.130",10000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(client_address)
while 1:
    data = input("input:")
    if not data:
        break
    s.sendto(data.encode("utf-8"), server_address)

    recivedata, addrg = s.recvfrom(2048)
    if recivedata:
        print("from:", addrg)
        print("got recive :", recivedata.decode())
s.close()
~~~

启动过后如下所示：

客户端发送：

~~~ruby
input:hello world
from: ('192.168.229.129', 10000)
got recive : my name is server
input:my name is client,hahaha
from: ('192.168.229.129', 10000)
got recive : woca
~~~

服务端接收：

~~~ruby
got data from ('192.168.229.130', 10000)
hello world
reply:my name is server
got data from ('192.168.229.130', 10000)
my name is client,hahaha
reply:woca
~~~