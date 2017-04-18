---
layout: post
categories: [scala]
title: scala的break和continue
date: 2017-04-13
author: TTyb
desc: "scala的break和continue"
---

`scala` 是没有 `continue` 的，但是包含 `break`，可以用 `break` 构造出 `continue` 的效果

这里用到了库：

```
import scala.util.control.Breaks.{break, breakable}
```

如果用 `breakable` 包裹整个循环，那么遇到 `break` 则是跳出整个循环：`breakable{for}` :

```
import scala.util.control.Breaks.{break, breakable}

object test {

  def main(args: Array[String]): Unit = {
    breakable {
      for (i <- 1 to 5) {
        if (i == 2) {
          //如果i=2则跳出循环
          break()
        }
        else {
          println(i)
        }
      }
    }
  }
}
```
打印结果：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170413142012126-563467794.png)

如果用 `for` 包裹 `breakable`，那么遇到 `break` 则是跳出本次循环：`for{breakable}` :

```
import scala.util.control.Breaks.{break, breakable}

object test {

  def main(args: Array[String]): Unit = {
    for (i <- 1 to 5) {
      breakable {
        if (i == 2) {
          //如果i=2则跳出循环
          break()
        }
        else {
          println(i)
        }
      }
    }
  }
}

```

打印结果：

![](http://images2015.cnblogs.com/blog/996148/201704/996148-20170413141946205-10920181.png)