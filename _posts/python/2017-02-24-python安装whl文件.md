---
layout: post
categories: [python]
title: python安装whl文件
date: 2017-02-24
author: TTyb
desc: "python安装万能仓库的whl文件出错，原来是文件名弄错了"
---

在命令指示符下(cmd)的Python3安装命令为：

~~~ruby
pip3 install 文件名.whl
~~~

<p style="text-align:center"><img src="/static/postimage/python/whl/996148-20170224083447570-949362846.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

安装出错：

~~~ruby
matplotlib-2.0.0-cp34-cp34m-win_amd64.whl is not a supported wheel on this platform.
~~~

原来是[万能仓库](http://www.lfd.uci.edu/~gohlke/pythonlibs/)的包名除了问题，将包的名字改一下就好：

`matplotlib-2.0.0-cp34-cp34m-win_amd64.whl` 改成 `matplotlib-2.0.0-cp34-none-win_amd64.whl`

完美安装：

<p style="text-align:center"><img src="/static/postimage/python/whl/996148-20170224084306257-1962765744.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

<p style="text-align:center"><img src="/static/postimage/python/whl/996148-20170224085315741-275552945.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>