#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

url = "http://www.tybai.com"
# url = "http://www.baidu.com"

html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")

print(html)
