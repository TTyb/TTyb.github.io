---
layout: post
categories: [javascript]
title: javascript操控浏览器
date: 2016-12-02
author: TTyb
desc: "javascript操控浏览器"
---

## 测试环境为Chrome浏览器47.0.2526.106 m

## 测试窗口为F12->Console

<p style="text-align:center"><img src="/static/postimage/javascrip/browser/996148-20161202144437974-1464200438.png" class="img-responsive center-block"/></p>

### 跳转网页

~~~ruby
// 跳转到百度
window.location.href = "https://www.baidu.com/"
~~~


~~~ruby
// 5秒后跳转
setTimeout(function(){
    location.href = "https://www.baidu.com/"
    },5000
)
~~~

### 填充输入框，点击百度一下

~~~ruby
document.getElementById("kw").value="TTyb";
form.submit();
~~~


~~~ruby
// 每隔5秒点击一次,点击3次
// 时间间隔出了错误，不明所以然，算不算是阿里月饼事件的伪代码
for (var i=0;i<3;i++){setTimeout(form.submit(),5000);alert("点击！")}
~~~

### 页面下拉到底

~~~ruby
// 简单版，不支持异步加载，快速
var y = 0;
while (y < document.body.scrollHeight){
window.scroll(0, y);
y += 10;
}
~~~


~~~ruby
// 复杂版，支持异步加载，缓慢
(function () {
    var y = 0;
    var step = 100;
    window.scroll(0, 0);

    function f() {
        if (y < document.body.scrollHeight) {
            y += step;
            window.scroll(0, y);
            setTimeout(f, 100);
        } else {
            window.scroll(0, 0);
            document.title += "scroll-done";
        }
    }

    setTimeout(f, 1000);
})();
~~~

### 清除控制台页面

~~~ruby
console.clear()
~~~

### 获取当前鼠标的坐标

~~~ruby
var x , y;
//当需求为获得的坐标值相对于body时
function positionBody(event){
	event = event||window.event;
	//获得相对于body定位的横标值
	x=event.clientX
	//获得相对于body定位的纵标值
	y=event.clientY
}

document.onmousemove = function(event){
	positionBody(event);
    console.log("(" + x + "," + y + ")");
}
~~~

<p style="text-align:center"><img src="/static/postimage/javascrip/browser/996148-20161202161520724-1585121090.png" class="img-responsive center-block"/></p>