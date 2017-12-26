---
layout: post
categories: [scala]
title: scala转换date提取年月日时分秒
date: 2017-04-25
author: TTyb
desc: "从数据库提取出来的时间为 `String` 格式，现在需要转换为 `date` 并提取出里面的 *小时* 时间段"
---

从数据库提取出来的时间为 `String` 格式，现在需要转换为 `date` 并提取出里面的 *小时* 时间段：

~~~ruby
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Calendar

object test {

  def main(args: Array[String]): Unit = {
    val datees = "2017-04-14 07:29:03.0"
    val hour = tranfTime(datees)
    println(hour)
  }

  def tranfTime(timestring: String): Int = {
    val fm = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
    //将string的时间转换为date
    val time: Date = fm.parse(timestring)

    val cal = Calendar.getInstance()
    cal.setTime(time)
    //提取时间里面的小时时段
    val hour: Int = cal.get(Calendar.HOUR)
    hour
  }
}

~~~