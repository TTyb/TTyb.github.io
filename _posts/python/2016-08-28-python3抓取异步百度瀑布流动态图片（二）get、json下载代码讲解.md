---
layout: post
categories: [python]
title: python3抓取异步百度瀑布流动态图片（二）get、json下载代码讲解
date: 2016-08-28
author: TTyb
desc: "详解如何搞定瀑布流"
---

制作解析网址的get;

~~~ruby
def gethtml(url,postdata):

    header = {'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                'Referer':
                'http://image.baidu.com',
                'Host': 'image.baidu.com',
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection':'keep-alive'}

    # 解析网页
    html_bytes = requests.get(url, headers=header,params = postdata)

    return html_bytes
~~~

头部的构造请参考上一篇博文

分析网址：

`http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=gif&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=gif&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=30&rn=30&gsm=1e&1472364207674=`

分解为：

`url = 'http://image.baidu.com/search/acjson?' + postdata + lasturl`

lasturl为时间戳，精确到后三位小数的时间戳，构造这个时间戳，后三位小数我就随机生成一个三位数了：

~~~ruby
import time
import random
timerandom = random.randint(100,999)
nowtime = int(time.time())
lasturl = str(nowtime) + str(timerandom) + '='
~~~

最后制作postdata：

~~~ruby
# 构造post
postdata = {
    'tn':'resultjson_com',
    'ipn':'rj',
    'ct':201326592,
    'is':'',
    'fp':'result',
    'queryWord': keyword,
    'cl': 2,
    'lm': -1,
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': -1,
    'z':'',
    'ic': 0,
    'word': keyword,
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': 0,
    'istype': 2,
    'qc': '',
    'nc': 1,
    'fr': '',
    'pn': pn,
    'rn': 30,
    'gsm': '1e'
}
~~~

其中页数pn和搜索关键字keywork为：

~~~ruby
# 搜索的关键字
# keywork = input('请输入你要查找的关键字')
keyword = 'gif'

# 页数
# pn = int(input('你要抓取多少页：'))
pn = 30
~~~

将得到的信息保存在本地，当所有都保存下来了再去下载图片：

~~~ruby
# 解析网址
contents = gethtml(url,postdata)

# 将文件以json的格式保存在json文件夹
file = open('../json/' + str(pn) + '.json', 'wb')
file.write(contents.content)
file.close()
~~~

读取文件夹里面的所有文件：

~~~ruby
# 找出文件夹下所有xml后缀的文件
def listfiles(rootdir, prefix='.xml'):
    file = []
    for parent, dirnames, filenames in os.walk(rootdir):
        if parent == rootdir:
            for filename in filenames:
                if filename.endswith(prefix):
                    file.append(rootdir + '/' + filename)
            return file
        else:
            pass
~~~

遍历json文件夹，读取里面的东西：

~~~ruby
# 找到json文件夹下的所有文件名字
files = listfiles('../json/', '.json')
for filename in files:
    print(filename)
    # 读取json得到图片网址
    doc = open(filename, 'rb')
    # ('UTF-8')('unicode_escape')('gbk','ignore')
    doccontent = doc.read().decode('utf-8', 'ignore')
    product = doccontent.replace(' ', '').replace('\n', '')
    product = json.loads(product)
~~~

查询字典data：

~~~ruby
# 得到字典data
onefile = product['data']
~~~

将字典里面的图片网址和图片名称放到数组里面：

<p style="text-align:center"><img src="/static/postimage/python/bdfalls2/996148-20160828165924367-733078421.png"/></p>

制作一个解析头来解析图片下载：

~~~ruby
def getimg(url):

    # 制作一个专家
    opener = urllib.request.build_opener()

    # 打开专家头部
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'),
                         ('Referer',
                          'http://image.baidu.com'),
                         ('Host', 'image.baidu.com')]
    # 分配专家
    urllib.request.install_opener(opener)

    # 解析img
    html_img = urllib.request.urlopen(url)

    return html_img
~~~

最后将图片下载到本地的gif文件夹：

~~~ruby
for item in onefile:
    try:
        pic = getimg(item['thumbURL'])
        # 保存地址和名称
        filenamep = '../gif/' + validateTitle(item['fromPageTitleEnc'] + '.gif')
        # 保存为gif
        filess = open(filenamep, 'wb')
        filess.write(pic.read())
        filess.close()

        # 每一次下载都暂停1-3秒
        loadimg = random.randint(1, 3)
        print('图片' + filenamep + '下载完成')
        print('暂停' + loadimg + '秒')
        time.sleep(loadimg)

    except Exception as err:
        print(err)
        print('暂停' + loadimg + '秒')
        time.sleep(loadimg)
        pass
~~~

得到效果如下：

<p style="text-align:center"><img src="/static/postimage/python/bdfalls2/996148-20160828172535915-551271077.png"/></p>

 本文只是编程，处理这种网址最重要的是思想，思想我写在上一篇博文
 
 思想有了，程序是很简单的问题而已。