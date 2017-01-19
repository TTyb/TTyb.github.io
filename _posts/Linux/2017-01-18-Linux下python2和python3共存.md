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


![](http://images2015.cnblogs.com/blog/996148/201701/996148-20170118111842734-1275144249.png)

下载命令：

```
wget https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tar.xz
```

解压：

```
tar xvf Python-3.4.4.tar.xz
```

进入目录：

```
cd Python-3.4.4
```

将其安装在 `/usr/local/` 里面：

```
./configure --prefix=/usr/local

make

make altinstall
```

如果出错：

```
checking for --enable-universalsdk... no
```

需要安装下面命令：

```
yum install gcc
```

如果出现pip3未安装的情况：

`Ignoring ensurepip failure: pip 7.1.2 requires SSL/TLS`

记得写入以下命令：

```
yum install openssl-devel
```

然后再：

```
make altinstall
```

python应用程序目录：

`/usr/local/bin/python3.4`

pip3的执行文件：

`/usr/local/bin/pip3.4 `

![](http://images2015.cnblogs.com/blog/996148/201701/996148-20170118145915796-428983248.png)


切记添加环境变量：

```
#set python3.4,pip3.4
   export PYTHON_HOME=/usr/local/bin/
```

让环境变量生效：

```
source /etc/profile
```

结果：

![](http://images2015.cnblogs.com/blog/996148/201701/996148-20170118150603750-802075189.png)