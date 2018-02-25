---
layout: post
categories: [python]
title: python日志syslog运用
date: 2017-03-22
author: TTyb
desc: "python日志syslog运用"
---

syslog的官方说明在：

> https://docs.python.org/2/library/syslog.html#module-syslog

该模块的主要方式为：

~~~ruby
#!/usr/bin/python
# -*- coding: utf-8 -*-

import syslog

syslog.openlog([ident[, logoption[, facility]]])
syslog.syslog(priority, message)
syslog.closelog()
~~~

`ident` 的信息为 `/bluedon/test.py`

`logoption` 的信息为 `[4642]`

`facility` 的信息为 `记录日志文件的位置` ，本文选取的 `facility = syslog.LOG_USER` ，即日志输出在 `/var/log/messages`

<p style="text-align:center"><img src="/static/postimage/python/syslog/996148-20170322143426486-250871748.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

源码为：

~~~ruby
#!/usr/bin/python
# -*- coding: utf-8 -*-
import syslog
import os

if __name__ == '__main__':
    # https://docs.python.org/2/library/syslog.html
    # syslog.openlog([ident[, logoption[, facility]]])

    # ident
    filename = os.path.abspath(__file__)

    # logoption
    # LOG_CONS：如果将信息发送给守护进程时发生错误，直接将相关信息输入到相关信息输出到终端。 
    # LOG_NDELAY：立即打开与系统日志的连接（通常情况下，只有在产生第一条日志信息的情况下才会打开与日志系统的连接） 
    # LOG_NOWAIT：在记录日志信息时，不等待可能的子进程的创建 
    # LOG_ODELAY：类似于LOG_NDELAY参数，与系统日志的连接只有在syslog函数调用时才会创建 
    # LOG_PID：每条日志信息中都包括进程号
    # LOG_PID, LOG_CONS, LOG_NDELAY, LOG_NOWAIT, LOG_PERROR
    pid = syslog.LOG_PID

    # facility
    # LOG_KERN, LOG_USER, LOG_MAIL, LOG_DAEMON, LOG_AUTH, LOG_LPR, LOG_NEWS, LOG_UUCP, LOG_CRON, LOG_SYSLOG, LOG_LOCAL0 to LOG_LOCAL7
    filepath = syslog.LOG_USER

    # Priority
    # LOG_EMERG, LOG_ALERT, LOG_CRIT, LOG_ERR, LOG_WARNING, LOG_NOTICE, LOG_INFO, LOG_DEBUG
    level = syslog.LOG_NOTICE

    # messages
    messages = "test start14"

    # syslog.openlog([ident[, logoption[, facility]]])
    syslog.openlog(filename, pid, filepath)
    # syslog.syslog(priority, message)
    syslog.syslog(level, messages)
    # close syslog
    syslog.closelog()
    
    # vim var/log/message
    # tail -f /tmp/syslog.txt
~~~

在不同机器上面查看结果：

<p style="text-align:center"><img src="/static/postimage/python/syslog/996148-20170322143426486-250871748.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

<p style="text-align:center"><img src="/static/postimage/python/syslog/996148-20170322143915252-167308740.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

将其写成了类

~~~ruby
#!/usr/bin/python
# -*- coding: utf-8 -*-
import syslog


class mysyslog(object):
    # level
    # LOG_EMERG, LOG_ALERT, LOG_CRIT, LOG_ERR, LOG_WARNING, LOG_NOTICE, LOG_INFO, LOG_DEBUG
    debug = syslog.LOG_DEBUG
    info = syslog.LOG_INFO
    notice = syslog.LOG_NOTICE
    warning = syslog.LOG_WARNING
    err = syslog.LOG_ERR
    crit = syslog.LOG_CRIT
    alert = syslog.LOG_ALERT
    emerg = syslog.LOG_EMERG

    # logoption
    # LOG_PID, LOG_CONS, LOG_NDELAY, LOG_NOWAIT, LOG_PERROR
    # LOG_CONS：如果将信息发送给守护进程时发生错误，直接将相关信息输入到相关信息输出到终端。
    # LOG_NDELAY：立即打开与系统日志的连接（通常情况下，只有在产生第一条日志信息的情况下才会打开与日志系统的连接）
    # LOG_NOWAIT：在记录日志信息时，不等待可能的子进程的创建
    # LOG_ODELAY：类似于LOG_NDELAY参数，与系统日志的连接只有在syslog函数调用时才会创建
    # LOG_PID：每条日志信息中都包括进程号
    cons = syslog.LOG_CONS
    ndelay = syslog.LOG_NDELAY
    nowait = syslog.LOG_NOWAIT
    pid = syslog.LOG_PID

    # facility
    # LOG_KERN, LOG_USER, LOG_MAIL, LOG_DAEMON, LOG_AUTH, LOG_LPR, LOG_NEWS, LOG_UUCP, LOG_CRON, LOG_SYSLOG, LOG_LOCAL0 to LOG_LOCAL7
    # kern = syslog.LOG_KERN
    # user = syslog.LOG_USER
    # mail = syslog.LOG_MAIL
    # daemon = syslog.LOG_DAEMON
    # auth = syslog.LOG_AUTH
    # lpr = syslog.LOG_LPR
    # news = syslog.LOG_NEWS
    # uucp = syslog.LOG_UUCP
    # cron = syslog.LOG_CRON
    # _syslog = syslog.LOG_SYSLOG

    @classmethod
    def __init__(self):
        pass

    @staticmethod
    def basicConfig(name, logoption):
        facility = syslog.LOG_USER
        syslog.openlog(name, logoption, facility)

    @staticmethod
    def tosyslog(level, ip, messages):
        newmessages = "[" + ip + "]" + " " + messages
        syslog.syslog(level, newmessages)

~~~