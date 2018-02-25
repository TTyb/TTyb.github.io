---
layout: post
categories: [git]
title: github pages绑定域名
date: 2017-05-06
author: TTyb
desc: "网上很多人问绑定域名要不要备案，很多人的回答是..."
---

网上很多人问 `github` 绑定域名要不要备案，很多人的回答是：

~~~ruby
国内主机需要备案，国外主机不用
~~~
这个说法是没错的，但是却没有直接回答出 `github pages` 是否需要备案！

首先声明 `github` 上面的博客空间属于国外空间，绑定域名可以 `不用备案` ！完全放心，作者买了域名还没备案也是可以用的 [百哥么么哒](http://www.tybai.com/)

为 `github pages` 绑定域名很简单，步骤如下：

# 1.购买域名

国内域名我选择了 *万网* ，进入界面搜索域名：

<p style="text-align:center"><img src="/static/postimage/git/yuming/996148-20170506193905773-492947689.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

**只需要域名即可** ，不需要买 **云解析**

# 2.域名实名认证

购买域名后需要对域名进行实名认证，只是上传 `身份证` 的正反面图片而已，很简单，一般1-2天就可以解决了：

<p style="text-align:center"><img src="/static/postimage/git/yuming/996148-20170506194209961-1869107179.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

# 3.为github增加解析

解析只需要增加如下格式就好：

<p style="text-align:center"><img src="/static/postimage/git/yuming/996148-20170506194411461-793018578.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>)

数字 `ip` 是 `ping` 自己 `github pages` 得到的：

<p style="text-align:center"><img src="/static/postimage/git/yuming/996148-20170506194630320-1062386731.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

# 4.为自己的github pages 绑定域名

在自己的博客里面增加文件 `CNAME`:

<p style="text-align:center"><img src="/static/postimage/git/yuming/996148-20170506194801867-863319396.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

里面的内容只是自己刚才购买的域名：

<p style="text-align:center"><img src="/static/postimage/git/yuming/996148-20170506194834976-1404139177.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

最后更新代码：

~~~ruby
git add --all
git commit -m "update"
git push
~~~

# 5.验证域名是否添加成功

进入自己的 `github pages` 设置，如果以下内容变化就代表成功了：

<p style="text-align:center"><img src="/static/postimage/git/yuming/996148-20170506195706773-1119336750.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

祝各位好运！


