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

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417175414852-819020746.png)

>Artifacts -> + -> jar -> From Modules with dependisies...

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417175522759-699187820.png)

选择需要打包的文件的 `Main` 函数所在路径文件：

>Main Class -> Ok

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417175927243-212182658.png)

切记这里还有一个位置是存放打包完成后的 `jar` 存放位置 `Output Directory` ：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417190747399-1810695351.png)

新建一个文件夹用于存放 `.MP` 文件，而且新建的文件夹一定要在 `src` 目录下！

> ![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417180424696-878136188.png)

然后 `yes`

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417184939196-1883591098.png)

更改 `jar` 包的名字，然后 `Apply`：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417185113790-1736070932.png)

可以看到出现了新的文件夹和文件：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417185213946-558849415.png)

> build -> build artifacts

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417185344774-194276525.png)

第一次建立选择 `build` ：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417185421368-1900752468.png)

下一次修改的时候就直接 `rebuild` 就可以了

将其传输到 `Linux` 目录下，运行命令删除不必要的文件：

```
zip -d 你的jar名字.jar META-INF/*.RSA META-INF/*.DSA META-INF/*.SF
```

然后输入命令运行：

```
bash spark-submit --class MF字段 你的jar名字.jar
```

其中 `MF字段` 为你的 `MF` 文件中的 `Main-Class` :

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170417190458790-523139930.png)