---
layout: post
categories: [git]
title: github pages代码高亮highlighter
date: 2017-12-27
author: TTyb
desc: "github pages一直想添加代码高亮highlighter，基于jekyll 3.0的rouge终于搞定了"
---

`github pages` 一直想添加代码高亮 `highlighter` ，基于 `jekyll 3.0` 的 `rouge` 终于搞定了：

<p style="text-align:center"><img src="/static/postimage/git/highlighter/20171227091833.jpg" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

### 下载代码高亮库

在 `cmd` 中输入：

~~~ruby
rougify style monokai.sublime > rouge.css
~~~

可以下载 `rouge.css` 出来，将这个 `css` 文件放到 `github pages` 项目中存放 `css` 的目录下，并在 `html` 中引用这个库，请自行更改引用的路径：

~~~ruby
<link href="/static/css/rouge.css" rel="stylesheet"/>
~~~

配置文件 `_config.yml` 中添加这些：

~~~ruby
markdown: kramdown
kramdown:
  syntax_highlighter: rouge
~~~

将博文 `md` 文件中的 ```` ``` ```` 替换为 `~~~ruby` ：

<p style="text-align:center"><img src="/static/postimage/git/highlighter/20171227093944.jpg" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

### 调试代码高亮

在 `cmd` 中安装 `rouge` 方便本地调试：

~~~ruby
gem install rouge
~~~

为了防止 ```` ` ```` 被转义，在 `html` 中添加如下 `js` ：

~~~ruby
<script type="text/x-mathjax-config">
MathJax.Hub.Config({tex2jax:{processEscapes: true, inlineMath: [ ['$','$'], ["\\(","\\)"] ], skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}});
MathJax.Hub.Config({TeX:{extensions: ["cancel.js", "enclose.js"],
Macros:{a:"\\alpha",b:"\\beta",c:"\\chi",d:"\\delta",e:"\\epsilon",f:"\\phi",g:"\\gamma",h:"\\eta",i:"\\iota",j:"\\varphi",k:"\\kappa",l:"\\lambda",m:"\\mu",n:"\\nu",o:"\\omicron",p:"\\pi",q:"\\theta",r:"\\rho",s:"\\sigma",t:"\\tau",u:"\\upsilon",v:"\\varpi",w:"\\omega",x:"\\xi",y:"\\psi",z:"\\zeta",D:"\\Delta",F:"\\Phi",G:"\\Gamma",J:"\\vartheta",L:"\\Lambda",P:"\\Pi",Q:"\\Theta",S:"\\Sigma",U:"\\Upsilon",V:"\\varsigma",W:"\\Omega",X:"\\Xi",Y:"\\Psi",ve:"\\varepsilon",vk:"\\varkappa",vq:"\\vartheta",vp:"\\varpi",vr:"\\varrho",vs:"\\varsigma",vf:"\\varphi",alg:"\\begin{align}", ealg:"\\end{align}",bmat:"\\begin{bmatrix}", Bmat:"\\begin{Bmatrix}", pmat:"\\begin{pmatrix}", Pmat:"\\begin{Pmatrix}", vmat:"\\begin{vmatrix}", Vmat:"\\begin{Vmatrix}",ebmat:"\\end{bmatrix}", eBmat:"\\end{Bmatrix}",  epmat:"\\end{pmatrix}",  ePmat:"\\end{Pmatrix}",  evmat:"\\end{vmatrix}",  eVmat:"\\end{Vmatrix}",AA:"\\unicode{x212B}", Sum:"\\sum\\limits", abs:['\\lvert #1\\rvert',1], rmd:['\\mathop{\\mathrm{d}#1}',1],bi:['\\boldsymbol{#1}', 1], obar:['0\\!\\!\\!\\raise{.05em}{-}'],opar:['\\frac{\\partial #1}{\\partial #2}', 2], oppar:['\\frac{\\partial^2 #1}{\\partial #2^2}', 2]}}});
MathJax.Hub.Queue(function(){
var all=MathJax.Hub.getAllJax(),i;for(i=0;i<all.length;i+=1){all[i].SourceElement().parentNode.className+=' has-jax';}});
</script>
~~~

在 `cmd` 中输入 `jekyll server`，本地打开 `127.0.0.1:4000` 查看代码是否高亮了：

<p style="text-align:center"><img src="/static/postimage/git/highlighter/20171227094219.jpg" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

背景色为白色，字段显示不出来，所以我把 `rouge.css` 的背景色改成了黑色，在 `rouge.css` 最后面添加如下代码：

~~~ruby
div[class="highlight"] > pre > code[class*="language-"] {
  background:black;
}
div[class="highlight"] > pre {
  background:black;
}
figure[class="highlight"] > pre > code[class*="language-"] {
  text-align:left;
  background:black;
}
figure[class="highlight"] > pre > code[class*="language-"] td > pre{
  text-align:left;
  background:black;
}
figure[class="highlight"] > pre {
  text-align:left;
  background:black;
}
div[class="highlighter-rouge"] > pre[class="highlight"] > code{
  background:black;
}
div[class="highlighter-rouge"] > pre[class="highlight"] {
  background:black;
}
~~~

最后效果图如最开始的图片那样了，可以在我的 [github pages](https://github.com/TTyb/TTyb.github.io) 代码中查看具体的详情