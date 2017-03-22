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

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import syslog

syslog.openlog([ident[, logoption[, facility]]])
syslog.syslog(priority, message)
syslog.closelog()
```

`ident` 的信息为 `/bluedon/test.py`

`logoption` 的信息为 `[4642]`

`facility` 的信息为 `记录日志文件的位置` ，本文选取的 `facility = syslog.LOG_USER` ，即日志输出在 `/var/log/messages`

![](http://images2015.cnblogs.com/blog/996148/201703/996148-20170322143426486-250871748.png)

源码为：

```
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
```

在不同机器上面查看结果：

![](http://images2015.cnblogs.com/blog/996148/201703/996148-20170322143426486-250871748.png)

![](http://images2015.cnblogs.com/blog/996148/201703/996148-20170322143915252-167308740.png)