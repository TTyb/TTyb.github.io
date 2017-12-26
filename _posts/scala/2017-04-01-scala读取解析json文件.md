---
layout: post
categories: [scala]
title: scala读取解析json文件
date: 2017-04-01
author: TTyb
desc: "scala读取解析json文件"
---

~~~ruby
import scala.util.parsing.json.JSON._
import scala.io.Source

object ScalaJsonParse {
  def main(args: Array[String]): Unit = {

    var tt =  Map.empty[String, Any]

    val tree = parseFull(Source.fromFile("/data/result.json").mkString)
    tt = tree match {
      case Some(map: Map[String, Any]) => map
    }
    println(tt.getClass.getSimpleName)

  }
}
~~~

得到的结果如下：

~~~ruby
HashTrieMap
~~~