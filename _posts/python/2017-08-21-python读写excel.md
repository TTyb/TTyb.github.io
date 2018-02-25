---
layout: post
categories: [python]
title: python读写excel
date: 2017-08-21
author: TTyb
desc: "记录python读写2003和2007版本的excel的一些方式"
---

在工作中往往需要读取 `excel` 文件，但是读取 `excel` 的方式很多，本文只列举集中比较好用的读写 `2003` 或者 `2007` 的方法：

<p style="text-align:center"><img src="/static/postimage/python/excel/0b7b02087bf40ad14cc91cbd5f2c11dfa9eccebb.jpg" class="img-responsive"/></p>

### 读取2007版本的excel

读取`xlsx` 需要用库 `openpyxl` ， 安装方式： `pip3 install openpyxl` 。设置 `excel` 的路径：

~~~ruby
excelPath = "F:/code/python/test.xlsx"
~~~

读取第一个 `Sheet` 表中的内容：

~~~ruby
# 仅仅读取Sheet1
workSheet = workBook.get_sheet_by_name("Sheet1")
~~~

这个库读取行和列是从 `1` 开始的，而不是从 `0` 开始的，所以设置初始的行和列都为 `1` :

~~~ruby
# 行、列的初始值
rownum = 1
columnnum = 1

# 获取第一行第一列单元格的值
cell = workSheet.cell(row=rownum, column=columnnum).value
print(cell)
~~~

当然也可以读取第二个 `Sheet` 表中的内容，只要将 `get_sheet_by_name` 改成 `Sheet2` 就行了。

### 写入2007版本的excel

写入 `xlsx` 需要用到库 `xlsxwriter` ，安装方式 `pip3 install xlsxwriter` 。新建或者是打开某个 `excel` ，我这里是新建一个 `excel` ：

~~~ruby
# 打开某个excel
with xlsxwriter.Workbook("F:/code/python/test1.xlsx") as workbook:
~~~

新建的 `Sheet` 的名字可以随便取，不是新建的要先读取当前 `Sheet` 的内容出来，再把自己的内容添加进去：

~~~ruby
# 设置Sheet的名字为haha
worksheet = workbook.add_worksheet("haha")
~~~

这个库读取行和列是从 `0` 开始的，而不是从 `1` 开始的。最后写入自己需要的值：

~~~ruby
# 行、列的初始值
rownum = 0
columnnum = 0
# 依次写入每个单元格
worksheet.write(rownum, columnnum, "one")
~~~

切记要关闭 `excel` :

~~~ruby
workbook.close()
~~~

### 读取2003版本的excel

读取`xls` 需要用库 `xlrd` ， 安装方式： `pip3 install xlrd` 。设置 `excel` 的路径：

~~~ruby
excelPath = "F:/code/python/test.xls"
~~~

加载 `excel` ：

~~~ruby
# 加载xlsx
wb = xlrd.open_workbook(excelPath)
~~~

读取第一个 `Sheet` 表中的内容：

~~~ruby
# 仅仅读取Sheet1
ws = wb.sheet_by_name("Sheet1")
~~~

这个库读取行和列是从 `0` 开始的，而不是从 `1` 开始的，所以设置初始的行和列都为 `0` :

~~~ruby
# 行、列的初始值
rownum = 0
columnnum = 0
# 获取第一行第一列单元格的值
cel = ws.cell(rowx=rownum, colx=columnnum).value
print(cel)
~~~

当然也可以读取第二个 `Sheet` 表中的内容，只要将 `sheet_by_name` 改成 `Sheet2` 就行了。

<a href="/static/postimage/python/excel/excel.py" target="_blank">excel.py</a>