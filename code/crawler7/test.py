#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import execjs

js='''function callback(){
        return 'bd__cbs__'+Math.floor(2147483648 * Math.random()).toString(36)
    }
    function gid(){
        return 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (e) {
        var t = 16 * Math.random() | 0,
        n = 'x' == e ? t : 3 & t | 8;
        return n.toString(16)
        }).toUpperCase()
    }'''
ctx = execjs.compile(js)
a = ctx.call("callback")
b = ctx.call("gid")
print(a)
print(b)