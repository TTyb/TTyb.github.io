---
layout: post
categories: [python]
title: flask下载excel
date: 2019-03-28
author: TTyb
desc: "在flask页面下载excel"
---

`flask` 应用的基本结构：

~~~ruby
htmlweb.py
    -- static
	-- templates
~~~

将 [bootstrap.min.css](https://www.tybai.com/static/css/bootstrap.min.css) 放到 `static` 文件夹下，在 `templates` 文件夹下新建 `index.html`，里面写入如下信息：

~~~ruby
<html>
<head>
    <title>APIParse</title>
    <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/bootstrap.min.css')}}"/>
</head>
<body>
TTYB
</body>
</html>
~~~

在 `htmlweb.py` 中写入如下内容：

~~~ruby
from flask import Flask, render_template
from io import BytesIO
import xlsxwriter
def create_workbook():
    output = BytesIO()
    # 创建Excel文件,不保存,直接输出
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    # 设置Sheet的名字为download
    worksheet = workbook.add_worksheet('download')
    # 列首
    title = ["col1","col2","col3"]
    worksheet.write_row('A1', title)
    dictList = [{"a":"a1","b":"b1","c":"c1"},{"a":"a2","b":"b2","c":"c2"},{"a":"a3","b":"b3","c":"c3"}]
    for i in range(len(dictList)):
        row = [dictList[i]["a"],dictList[i]["b"],dictList[i]["c"]]
        worksheet.write_row('A' + str(i + 2), row)
    workbook.close()
    response = make_response(output.getvalue())
    output.close()
    return response


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

from flask import make_response
@app.route('/download', methods=['GET'])
def download():

    response = create_workbook()
    response.headers['Content-Type'] = "utf-8"
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Content-Disposition"] = "attachment; filename=download.xlsx"
    return response

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=88, debug=True)
~~~

运行在浏览器访问 [127.0.0.1:88](127.0.0.1:88) 可以看到新建的页面，在页面访问 [127.0.0.1/download](127.0.0.1/download) 可以下载生成的 `excel` :

<p style="text-align:center"><img src="/static/postimage/python/flask/20190328153426.jpg" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>