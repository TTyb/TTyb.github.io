---
layout: post
categories: [python]
title: python连接Linux命令行
date: 2017-03-21
author: TTyb
desc: "python连接Linux命令行"
---

~~~ruby
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pexpect
import types


username = "root"
ip = "192.168.***.***"
password = "****"
pex = pexpect.spawn('ssh %s@%s' % (username, ip))


def _check(pattern, timeout=120):
    i = pex.expect(pattern, timeout=timeout)
    return i


def sendcr(cmd):
    if pex == None:
        return 0
    n = pex.send("%s\r" % cmd)
    return n


def getexec(cmd):

    child = pexpect.spawn(cmd)
    child.expect(pexpect.EOF)
    return child.before


if __name__ == '__main__':

    checklist1 = [["(?i)Connection refused", False],
                  ["(?i)Host key verification failed.", False],
                  ["(?i)VENUSTECH AUDIT SYSTEM MA1000", True],
                  # ["(?i)#\[/]",True],        # hpux
                  ["(?i).+>", True],  # windows
                  [".+[>$#]\s*$", True],  # debian
                  ["(?i)Last login", True],
                  ["(?i)access denied", False],
                  ["(?i)NT_STATUS_LOGON_FAILURE", False],
                  ["(?i)are you sure you want to continue connecting", "yes"],
                  ["(?i)authentication fail(?!ure)", False],
                  ["(?i)connection closed by remote host", False],
                  ["(?i)login failed", False],
                  ["(?i)login incorrect", False],
                  ["(?i)need to be root", False],
                  ["(?i)no route to host", False],
                  ["(?i)not found", False],
                  ["(?i)Bad secrets", False],
                  ["(?i)incorrect password", False],
                  ["(?i)permission denied", False],
                  # ["(?i)terminal type",terminal_type],
                  ["This private key will be ignored.", False],
                  ["(?i)no route to host", False],
                  ["(?i)press 'Enter' key to proceed", "\r"],
                  ["(?i)Y/N", 'Y'],
                  [pexpect.EOF, False],
                  [pexpect.TIMEOUT, False],
                  ["(?i)Enter passphrase for key .*:", password],
                  ["(?i)assword", password],
                  ["(?i)passwd", password],
                  ["(?i)sername", username],
                  ["(?i)(?<!sful )login", username],
                  ["(?i)----------------------------------------------------------------", True]]

    checklist2 = [i[0] for i in checklist1]
    while True:
        i = _check(checklist2)
        print i, checklist1[i], checklist1[i][1]
        if (type(checklist1[i][1]) is types.BooleanType):
            if type(checklist1[i][1]):
                break
        else:
            sendcr(checklist1[i][1])

    cmd = "ls -l /etc/rsyslog.conf"
    result = getexec(cmd)
    print "result", result
~~~

打印结果：

~~~ruby
26 ['(?i)assword', '***'] ***
5 ['(?i)Last login', True] True
result -rw-r--r--. 1 root root 3167 Mar 13 11:24 /etc/rsyslog.conf
~~~