---
layout: post
categories: [python]
title: python的StringIO
date: 2017-03-22
author: TTyb
desc: "python的StringIO"
---

有时候需要将 `information` 保存在本地，可以这样写：

```
file = open("filename","w")
file.close()
file.close()
```

但是有时候不想写到本地，只是要存在电脑内存就好，这样就可以用 `StringIO` 进行保存：

```

import StringIO
s = StringIO.StringIO()
s.write(messages)
s.seek(0)
getmessages = s.read()
s.close()
```

`StringIO` 可以有按行读取 `readlines` ，按行写入 `writelines` ,一般操作文件写入的方法都会有，具体请看：

>https://docs.python.org/2/library/stringio.html