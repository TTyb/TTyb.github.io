---
layout: post
categories: [scala]
title: scala打包jar并在Linux下运行
date: 2017-04-17
author: TTyb
desc: "scala打包jar并在Linux下运行"
---

打开

>File -> Project Structure

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417175414852-819020746.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

>Artifacts -> + -> jar -> From Modules with dependisies...

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417175522759-699187820.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

选择需要打包的文件的 `Main` 函数所在路径文件：

>Main Class -> Ok

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417175927243-212182658.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

新建一个文件夹用于存放 `.MP` 文件，而且新建的文件夹一定要在 `src` 目录下！

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417180424696-878136188.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

然后 `yes`

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417184939196-1883591098.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

更改 `jar` 包的名字，然后 `Apply`：

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170427143303006-312290811.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

切记这里还有一个位置是存放打包完成后的 `jar` 存放位置 `Output Directory` ：

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417190747399-1810695351.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

可以看到出现了新的文件夹和文件：

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417185213946-558849415.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

> build -> build artifacts

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417185344774-194276525.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

第一次建立选择 `build` ：



下一次修改的时候就直接 `rebuild` 就可以了

将其传输到 `Linux` 目录下，运行命令删除不必要的文件：

~~~ruby
zip -d 你的jar名字.jar META-INF/*.RSA META-INF/*.DSA META-INF/*.SF
~~~

然后输入命令运行：

~~~ruby
bash spark-submit --class MF字段 你的jar名字.jar
~~~

其中 `MF字段` 为你的 `MF` 文件中的 `Main-Class` :

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170417190458790-523139930.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

如果出现错误：

<p style="text-align:center"><img src="/static/postimage/scala/jar/996148-20170418105700227-405385447.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>

请自行添加 `bash` 的环境变量