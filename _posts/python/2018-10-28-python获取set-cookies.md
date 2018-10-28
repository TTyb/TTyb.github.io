---
layout: post
categories: [python]
title: python获取set-cookies
date: 2018-10-28
author: TTyb
desc: "python获取set-cookies"
---

~~~ruby
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import requests

url = "https://www.baidu.com/"
session = requests.session()
session.get(url)
html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
print(html_set_cookie)
~~~

~~~ruby
{'BDORZ': '27315'}
~~~