---
layout: post
categories: [python]
title: subprocess实时获取结果和捕获错误
date: 2018-11-01
author: TTyb
desc: "需要调用命令行来执行某些命令，主要是用subprocess实时获取结果和捕获错误，发现subprocess的很多坑"
---

需要调用命令行来执行某些命令，主要是用 `subprocess` 实时获取结果和捕获错误，发现subprocess的很多坑。

`subprocess` 普通获取结果方式，其需要命令完全执行才能返回结果：

~~~ruby
import subprocess

scheduler_order = "df -h"
return_info = subprocess.Popen(scheduler_order, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

for next_line in return_info.stdout:
    return_line = next_line.decode("utf-8", "ignore")
    print(return_line)
~~~

客`subprocess` 实时获取结果：

~~~ruby
import subprocess

scheduler_order = "df -h"
return_info = subprocess.Popen(scheduler_order, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
while True:
    next_line = return_info.stdout.readline()
    return_line = next_line.decode("utf-8", "ignore")
    if return_line == '' and return_info.poll() != None:
        break
    print(return_line)
~~~

想要获取报错机制，使用 [check_output](https://stackoverflow.com/questions/24849998/how-to-catch-exception-output-from-python-subprocess-check-output) 捕捉报错和使用 [check_call](https://stackoverflow.com/questions/29580663/save-error-message-of-subprocess-command) 捕捉报错，及时在 [Popen](https://stackoverflow.com/questions/15316398/check-a-commands-return-code-when-subprocess-raises-a-calledprocesserror-except) 中捕获报错，都会使 **实时输出失效** ！，所以自行查看 `CalledProcessError` 源码终于搞定。

实时发送以及捕获报错：

~~~ruby
import subprocess

try:
    scheduler_order = "top -u ybtao"
    return_info = subprocess.Popen(scheduler_order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        next_line = return_info.stdout.readline()
        return_line = next_line.decode("utf-8", "ignore")
        if return_line == '' and return_info.poll() != None:
            break
        print(return_line)

    returncode = return_info.wait()
    if returncode:
        raise subprocess.CalledProcessError(returncode, return_info)
except Exception as e:
    print(e)
~~~
