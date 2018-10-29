---
layout: post
categories: [Linux]
title: Python3+Flask+uwsgi部署
date: 2018-8-29
author: TTyb
desc: "Python3+Flask+uwsgi部署web服务，实现在新的IP下打开网址"
---

# python3

按照常规的方式安装即可：

~~~ruby
wget https://www.python.org/ftp/python/3.5.4/Python-3.5.4.tgz
tar zxvf Python-3.5.4.tgz
cd Python-3.5.4/
./configure
make -j4
make install
~~~

添加环境变量

~~~ruby
vim /etc/profile
PYTHONPATH=/usr/local/lib/python3.5/bin
~~~

修改 `yum` 的python

~~~ruby
vim /usr/bin/yum
#!/usr/bin/python -> #!/usr/bin/python2.7
~~~

# Flask

~~~ruby
pip3 install flask
~~~

# uwsgi

~~~ruby
wget https://pypi.python.org/packages/0c/1c/44849e293e367a157f1ad863cee02b4b865840543254d8fae3ecdebdbdb9/uwsgi-2.0.12.tar.gz
~~~

我的网页的路径为：

~~~ruby
/home/APIParse
/home/APIParse/htmlWeb.py
...
~~~

<p style="text-align:center"><img src="/static/postimage/linux/uwsgi/996148-20180829151953301-1195845668.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

在当前路径下新建`uwsgiconfig.ini`，写入如下信息

~~~ruby
[uwsgi]
# htmlWeb.py文件所在目录
chdir           = /home/APIParse

callable = app

# flask文件名
wsgi-file= htmlWeb.py

# 进程数
processes       = 5

# 使用3993端口
http = 0.0.0.0:3993

# 日志输出目录
daemonize = /home/APIParse/flask.log

pidfile = project-master.pid
~~~

完成保存退出，启动命令并查看进程：

~~~ruby
# 启动命令
uwsgi uwsgi.ini
 # 查看进程是否启动成功
ps -ef | grep uwsgi
~~~

<p style="text-align:center"><img src="/static/postimage/linux/uwsgi/996148-20180829152034067-1379964892.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

如果想要停止uwsgi，就可以杀死所有：

~~~ruby
killall -9 uwsgi
~~~