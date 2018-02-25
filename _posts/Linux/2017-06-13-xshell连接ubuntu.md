---
layout: post
categories: [Linux]
title: xshell连接ubuntu
date: 2017-06-13
author: TTyb
desc: "安装了 `ubuntu-14` ，为了连接 `xshell` ，做出的一些配置"
---

安装了 `ubuntu-14` ，为了连接 `xshell` ，做出的一些配置如下：

### 1.激活root用户

~~~ruby
sudo passwd root
~~~

设置新密码，设置成功后会有提示 `passwd：password updated sucessfully`

### 2.安装ssh服务

~~~ruby
apt-get install ssh
~~~

### 3.设置root密码登陆

~~~ruby
vi /etc/ssh/sshd_config
~~~

将

~~~ruby
# Authentication:
LoginGraceTime 120
PermitRootLogin prohibit-password
StrictModes yes
~~~

改成：

~~~ruby
# Authentication:
LoginGraceTime 120
PermitRootLogin yes
StrictModes yes
~~~

### 4.使配置生效


安装完毕后重启 `ssh` 服务：

~~~ruby
重启
~~~

`or`

~~~ruby
service sshd start
~~~

`or`

~~~ruby
/etc/init.d/sshd start
~~~

### 5.验证ssh是否开启

~~~ruby
ps -ef | grep ssh
~~~

最后就可以用 `xshell` 连接了

> 以下为找到 `ubuntu` 控制台位置：

找到按钮：

<p style="text-align:center"><img src="/static/postimage/linux/ubuntu/996148-20170613091751900-2125513854.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

点击第二个：

<p style="text-align:center"><img src="/static/postimage/linux/ubuntu/996148-20170613091909181-1334363079.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

点击第二行：

<p style="text-align:center"><img src="/static/postimage/linux/ubuntu/996148-20170613091949618-1950325186.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

找到控制台：

<p style="text-align:center"><img src="/static/postimage/linux/ubuntu/996148-20170613092024415-1043489570.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

打开，在桌面右键 -> Lock to Launcher

<p style="text-align:center"><img src="/static/postimage/linux/ubuntu/996148-20170613092140728-675904521.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>