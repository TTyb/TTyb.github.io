---
layout: post
categories: [scala]
title: scala调用Linux命令行
date: 2017-05-22
author: TTyb
desc: "在scala里面存在 调用Linux命令行的函数，得到返回的结果"
---

在 `scala` 里面存在 调用 `Linux` 命令行的函数：

```
import scala.sys.process._
```

执行的方法也不难：

```
import scala.sys.process._

/**
  * Created by TTyb on 2017/5/22.
  */
object test1 {
  def main(args: Array[String]): Unit = {
    val cmd = "history"
    val result = cmd.!!
    // 查看返回的结果
    println(result)
  }

}
```

需要注意的是，这个库只能调用 `Linux` 的命令行，在 `Windows` 下不行
