---
layout: post
categories: [scala]
title: scala用ssh2连接Linux
date: 2017-05-22
author: TTyb
desc: "在scala中远程连接Linux，并发送相关命令到Linux上，得到返回的结果"
---

这个需要安装库：

~~~ruby
import ch.ethz.ssh2.{Connection, Session, StreamGobbler}
~~~

首先用 `ip` 和 `post` 创建连接：

~~~ruby
val conn: Connection = new Connection(ipAddr, post)
~~~

判断这个连接是否连接上了，这个用了一个 `Boolean` 类型判断：

~~~ruby
def login(): Boolean = {
    conn.connect()
    // 连接
    val ret: Boolean = conn.authenticateWithPassword(userName, password)
    ret
  }
~~~

如果连接成功的话，那么就将命令发送过去，命令发送只需要建立一个会话即可，执行命令返回的值保存在 `in` 中：

~~~ruby
val session = conn.openSession()
session.execCommand(cmds)
val in = session.getStdout
~~~

最后就是处理解析 `in` 中的返回结果就行了：

~~~ruby
val is = new StreamGobbler(in)
val brs: BufferedReader = new BufferedReader(new InputStreamReader(is))
val line = brs.lines().toArray().toList.mkString(",")
~~~

完整的类封装成：

~~~ruby
class RemoteShellTool(ipAddr: String, post: Int, userName: String, password: String) {

  val conn: Connection = new Connection(ipAddr, post)

  //判断是否连接上了
  def login(): Boolean = {
    conn.connect()
    // 连接
    val ret: Boolean = conn.authenticateWithPassword(userName, password)
    ret
  }

  //发送命令过去
  def exec(cmds: String): String = {
    var result: String = ""
    try {
      val str_ret: Boolean = login()
      if (str_ret) {
        // 打开一个会话
        val session = conn.openSession()
        session.execCommand(cmds)
        val in = session.getStdout
        result = processStdout(in)
      } else {
        println("连接失败")
      }
    } catch {
      case e: IOException => {
        e.printStackTrace()
      }
    } finally {
      conn.close()
    }
    result
  }

  //处理返回结果
  def processStdout(in: InputStream): String = {
    val is = new StreamGobbler(in)
    val brs: BufferedReader = new BufferedReader(new InputStreamReader(is))
    val line = brs.lines().toArray().toList.mkString(",")
    line
  }
~~~

在 `main` 函数中调用这个类即可：

~~~ruby
def main(args: Array[String]): Unit = {

    //读取配置文件
    val filePath = System.getProperty("user.dir")
    val properties: Properties = new Properties()
    val ipstream = new BufferedInputStream(new FileInputStream(filePath + "/conf/configssh.properties"))
    properties.load(ipstream)

    val ip = "ip"
    val post = "post".toInt
    val userName = "userName"
    val password = password"
    val cmd = "cmd"

    val rms = new RemoteShellTool(ip, post, userName, password)
    val result = rms.exec(cmd)
    println(result)
  }
~~~

这个方法能发送的 `cmd` 有点少，比如能识别 `date` 、 `ls` 等，但是不能识别 `history` 、 `ll`