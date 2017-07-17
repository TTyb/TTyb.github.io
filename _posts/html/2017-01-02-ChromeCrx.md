---
layout: post
categories: [html]
title: ChromeCrx
date: 2017-01-02
author: TTyb
desc: "学习了一些chrome插件的基本用法"
---

### 文件夹目录为：

```
-- images

---- icon38.png

-- js

---- jquery.min.js

---- test.js

manifest.json
```

`images` 是存放插件图标的

`js` 是网页的javascript文件，其中test.js的代码为：

```
function httpRequest(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            callback(xhr.responseText);
        }
    };
    xhr.onerror = function () {
        callback(false);
    };
    xhr.send();
}

try {
    var goodsid=$("meta[content*='shopId']").attr("content").split("shopId=")[1].split(";")[0];
} catch (e) {}

var InsertNode = "<div><span>这里是商品的id<a href='https://ttyb.github.io' target='_blank' class='mnav'>" + goodsid + "</a></span>" +
                    "<hr><span>这里用api提取出该id下的商品信息<span>" +
                    "<hr><small>百哥么么哒</small>" +
                    "<p>没有写css所以很难看</span>" +
                    "<h6>我没有淘宝客的api权限</h6></div>"

var InsertionPoint=$("#J_StrPriceModBox").parent();
$(InsertionPoint).append(InsertNode);

//httpRequest("apiurl", function (returninfo) {
//    apireturn = returninfo
//}

//json解析
//var json = {
//    contry: {
//        area: {
//            man: "12万",
//            women: "10万"
//        }
//    }
//};
//var obj = eval(json);
//alert(obj.contry.area.women);
```

`manifest.json` 为配置文件，配置文件请查考api文档 [Chrome开发文档](http://open.chrome.360.cn/extension_dev/overview.html)

最后的效果为：

<p style="text-align:center"><img src="/static/postimage/html/crx/996148-20170102103715284-478700539.jpg"/></p>

本文相当于提供思路，写的代码也很不完整，相当于伪代码，源码请看我的 [github](https://github.com/TTyb/mycrx)