---
layout: post
categories: [Linux]
title: Linux下python2和python3共存
date: 2017-01-18
author: TTyb
desc: "在Linux下安装python3且不影响系统的python2"
---

python下载地址：

`https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tar.xz`


<p style="text-align:center"><img src="/static/postimage/linux/python23/996148-20170118111842734-1275144249.png" class="img-responsive center-block"/></p>

下载命令：

~~~ruby
wget https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tar.xz
~~~

解压：

~~~ruby
tar xvf Python-3.4.4.tar.xz
~~~

进入目录：

~~~ruby
cd Python-3.4.4
~~~

将其安装在 `/usr/local/` 里面：

~~~ruby
./configure --prefix=/usr/local

make

make altinstall
~~~

如果出错：

~~~ruby
checking for --enable-universalsdk... no
~~~

需要安装下面命令：

~~~ruby
yum install gcc
~~~

如果出现pip3未安装的情况：

`Ignoring ensurepip failure: pip 7.1.2 requires SSL/TLS`

记得写入以下命令：

~~~ruby
yum install openssl-devel
~~~

然后再：

~~~ruby
make altinstall
~~~

python应用程序目录：

`/usr/local/bin/python3.4`

pip3的执行文件：

`/usr/local/bin/pip3.4 `

<p style="text-align:center"><img src="/static/postimage/linux/python23/996148-20170118145915796-428983248.png" class="img-responsive center-block"/></p>


切记添加环境变量：

~~~ruby
#set python3.4,pip3.4
   export PYTHON_HOME=/usr/local/bin/
~~~

让环境变量生效：

~~~ruby
source /etc/profile
~~~

结果：

<p style="text-align:center"><img src="/static/postimage/linux/python23/996148-20170118150603750-802075189.png" class="img-responsive center-block"/></p>

`yum` 命令不兼容 `Python3` ，需要指定为原版本 `Python2.x` ， `x` 需要自己确定：

~~~ruby
vim /usr/bin/yum
~~~

将文件中 `"!/usr/bin/python"` 改为 `"!/usr/bin/python2.x"` ， `x` 需要自己确定。
